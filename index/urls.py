"""

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from index import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('project',views.project, name='project'),
    path('contact',views.contact, name='contact'),
    
    
    
    
    ]
