from omniply.apps.decisions.abstract import CHOICE

from .imports import *


class Rule(MultiGadgetBase):
	_kind_registry = Class_Registry()
	@classmethod
	def find(cls, kind: str):
		return cls._kind_registry.get_class(kind)


	def __init_subclass__(cls, kind: str = None, **kwargs):
		super().__init_subclass__(**kwargs)
		if kind is not None:
			cls._kind_registry.new(kind, cls)


	_fill_in_abstract = False
	@classmethod
	def set_abstraction(cls, fill_in_abstract: bool = None):
		if fill_in_abstract is None:
			fill_in_abstract = not cls._fill_in_abstract
		cls._fill_in_abstract = fill_in_abstract
		return cls._fill_in_abstract


	_part_key_fmt = 'p{}'
	def _process_parts(self, raw_parts: Iterable[str | int]) -> list[str]:
		parts = [self._part_key_fmt.format(part) if isinstance(part, int) else part for part in raw_parts]
		return parts


	_fixed_num_parts = None
	def __init__(self, name: str, parts: list[str | int] | tuple = (), **kwargs):
		if len(parts):
			parts = self._process_parts(parts)
		if self._fixed_num_parts is not None:
			assert len(parts) == self._fixed_num_parts, (f'{self.__class__.__name__} expects '
														 f'{self._fixed_num_parts} parts, '
														   f'but got {len(parts)}: {parts}')
		super().__init__(**kwargs)
		self._name = name
		self._parts = tuple(parts)


	@property
	def name(self):
		return self._name


	@property
	def parts(self):
		return self._parts


	@property
	def num_parts(self):
		return len(self.parts)


	@property
	def is_abstract(self):
		return self._fill_in_abstract


	def _as_abstract(self, ctx: 'AbstractGame'):
		raise NotImplementedError


	def grab_from(self, ctx: 'AbstractGame', gizmo: str) -> Any:
		if gizmo == self.name and self.is_abstract:
			out = self._as_abstract(ctx)
			if out is not None:
				return out
		return super().grab_from(ctx, gizmo)



class RuleTemplate(Rule, Template):
	def __init__(self, name: str, parts: list[str | int] = (), gizmo=None, **kwargs):
		if gizmo is None:
			gizmo = name
		super().__init__(name, parts, template=None, gizmo=gizmo, **kwargs)


	@property
	def template(self):
		if self._template is None:
			self._template = self._build_template(self._base_template, self.parts)
		return self._template


	_base_template = None
	@staticmethod
	def _build_template(base_template: str, parts: Iterable[str]) -> str:
		'''
		Returns a template trivially filled in with the given arguments.

		Args:
			base_template (str): The template to fill in with indexed arguments (eg. '{0}{1}').
			args (str): The arguments to fill in, generally should be gizmos (eg. 'p1', 'p2').

		Returns:
			str: A template that can be used to generate a gizmo.
		'''
		if base_template is None:
			base_template = ''.join(f'{{{i}}}' for i in range(len(parts)))
		fixed = [part if part.endswith('}') and part.startswith('{') else f'{{{part}}}' for part in parts]
		return base_template.format(*fixed)


	def _as_abstract(self, ctx: 'AbstractGame'):
		reqs = {key: f'{{{key}}}' for key in self.parts}
		return self.fill_in(reqs)



class Point(RuleTemplate, kind='point'):
	_fixed_num_parts = 1
	_part_key_fmt = 'arg{}'

	def _as_abstract(self, ctx: 'AbstractGame'):
		reqs = {key: f'{{{key}}}'.replace('arg', 'p') for key in self.parts}
		return self.fill_in(reqs)



class Line(RuleTemplate, kind='line'):
	_fixed_num_parts = 2
	_base_template = 'line {0}{1}'


class Angle(RuleTemplate, kind='angle'):
	_fixed_num_parts = 3
	_base_template = '∠{0}{1}{2}'


class Triangle(RuleTemplate, kind='triangle'):
	_fixed_num_parts = 3
	_base_template = 'triangle {0}{1}{2}'


class Circle(RuleTemplate, kind='circle'):
	_fixed_num_parts = 4
	# _base_template = 'circle {1}{2}{3} centered at {0}'
	_base_template = 'circle {0}{1}{2}{3}'


class _Circle(RuleTemplate, kind='_circle'):
	_fixed_num_parts = 2
	_base_template = 'circle centered at {0} with radius {0}{1}'


class Quadrilateral(RuleTemplate, kind='quadrilateral'):
	_fixed_num_parts = 4
	_base_template = 'quadrilateral {0}{1}{2}{3}'


class Trapezoid(RuleTemplate, kind='trapezoid'):
	_fixed_num_parts = 4
	_base_template = 'trapezoid {0}{1}{2}{3}'


class Parallelogram(RuleTemplate, kind='parallelogram'):
	_fixed_num_parts = 4
	_base_template = 'parallelogram {0}{1}{2}{3}'


class Rhombus(RuleTemplate, kind='rhombus'):
	_fixed_num_parts = 4
	_base_template = 'rhombus {0}{1}{2}{3}'


class Rectangle(RuleTemplate, kind='rectangle'):
	_fixed_num_parts = 4
	_base_template = 'rectangle {0}{1}{2}{3}'


class Square(RuleTemplate, kind='square'):
	_fixed_num_parts = 4
	_base_template = 'square {0}{1}{2}{3}'



# Special (complex) rules

from .common import Enumeration


class ComplexRule(Rule):
	def _as_abstract(self, ctx: 'AbstractGame'):
		ctx[f'{self.name}_order'] = 0
		for key in self.parts:
			ctx[key] = f'{{{key}}}'
		return # none to default to previous behavior



class Conjunction(ComplexRule, ToolKit, kind='conjunction'):
	_term_options = [' and ', ' & ', None] # TODO: maybe split up to properly manage the oxford comma

	def __init__(self, name: str, elements: list[str], ordered=False, **kwargs):
		super().__init__(name, elements, **kwargs)
		self.include(SimpleDecision(f'{name}_term', self._term_options))
		self.include(Enumeration(elements, gizmo=name, oxford=True, ordered=ordered,
								 aggregator_gizmo=f'{name}_term', choice_gizmo=f'{name}_order'))


	def _as_abstract(self, ctx: 'AbstractGame'):
		ctx[f'{self.name}_term_choice'] = 0
		return super()._as_abstract(ctx)



class OrderedConjunction(Conjunction, kind='ord-conjunction'):
	def __init__(self, name: str, elements: list[str], **kwargs):
		super().__init__(name, elements, ordered=True, **kwargs)



	def _as_abstract(self, ctx: 'AbstractGame'):
		return super()._as_abstract(ctx)


class Equality(ComplexRule, ToolKit, kind='equality'):
	def __init__(self, name: str, elements: list[str], **kwargs):
		super().__init__(name, elements, **kwargs)

		options = []

		eqsign = Enumeration(elements, delimiter=' = ', gizmo=name, choice_gizmo=f'{name}_order')
		options.append(eqsign)

		if len(elements) > 2:
			terms = SimpleDecision(f'{name}_term', [' all equal ', ' are all the same as ', ' are all congruent to '])
			order = Enumeration(elements, gizmo=name, aggregator_gizmo=f'{name}_term', choice_gizmo=f'{name}_order')
			options.append(ToolKit().include(terms, order))
		elif len(elements) == 2:
			terms = SimpleDecision(f'{name}_term', [' equals ', ' is equal to ', ' is the same as ', ' is congruent to '])
			order = Enumeration(elements, gizmo=name, aggregator_gizmo=f'{name}_term', choice_gizmo=f'{name}_order')
			options.append(ToolKit().include(terms, order))

		self.include(GadgetDecision(options, choice_gizmo=f'{name}_fmt') if len(options) > 1 else options[0])


	def _as_abstract(self, ctx: 'AbstractGame'):
		ctx[f'{self.name}_fmt'] = 0
		return super()._as_abstract(ctx)



class Disjunction(ComplexRule, Enumeration, kind='disjunction'):
	_aggregator = ' or '

	def __init__(self, name: str, elements: list[str], **kwargs):
		super().__init__(name, elements, oxford=True, element_gizmos=elements, gizmo=name,
						 choice_gizmo=f'{name}_order', **kwargs)



class LiteralRule(Rule, SimpleDecision, kind='literal'):
	def __init__(self, name: str, options: list[str], **kwargs):
		super().__init__(name, options, choices=options, gizmo=name, **kwargs)


	def _as_abstract(self, ctx: 'AbstractGame'):
		return # behavior unchanged



class ReferenceRule(LiteralRule, kind='ref'):
	def __init__(self, name: str, options: list[str], **kwargs):
		super().__init__(name, options, **kwargs)


	# def _as_abstract(self, ctx: 'AbstractGame'):
	# 	return super()._commit(ctx, ctx[self.choice_gizmo], self.name)


	def _commit(self, ctx: 'AbstractGame', choice: CHOICE, gizmo: str) -> Any:
		return ctx.grab(super()._commit(ctx, choice, gizmo))


class SubTemplates(Rule, GadgetDecision, kind='sub'):
	_Template = Template
	def __init__(self, name: str, templates: list[str], **kwargs):
		gadgets = [self._Template(template) for template in templates]
		super().__init__(name, templates, choices=gadgets, choice_gizmo=f'{name}_choice', **kwargs)


	def _as_abstract(self, ctx: 'AbstractGame'):
		return ctx[self.choice_gizmo]





