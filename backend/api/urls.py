from django.urls import path
from .views import ProblemListView, SolveProblemNoImgView, SolveWithPSPG, Viewdata, CheckData, SolveInter
from rest_framework import routers 
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from django.views.generic import RedirectView
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Problem API",
        default_version='v1',
    ),
    url=settings.HOST,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('problems/', ProblemListView.as_view(), name='problem_list'),
    path('problems/solve_no_img/', SolveProblemNoImgView.as_view(), name='solve_problem'),
    path('problems/viewdata/', Viewdata.as_view(), name='viewdata'),
    path('problems/solve_pgps/', SolveWithPSPG.as_view(), name='solve_pgps'),
    path('problems/check_data', CheckData.as_view(),name = 'check_data'),
    path('problems/solve_inter', SolveInter.as_view(),name = 'solve_inter'),
]
