from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "curd.HodViews":
                    pass
                elif modulename == "curdopt.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_home")

            elif user.user_type == "2":
                if modulename == "curdopt.StaffViews":
                    pass
                elif modulename == "curdopt.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("staff_home")

            elif user.user_type == "3":
                if modulename == "curdopt.StudentViews":
                    pass
                elif modulename == "curdopt.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("student_home")

            else:
                return redirect("adminlogin")

        else:
            if request.path == reverse("adminlogin") or request.path == reverse("adminlogin"):
                pass
            else:
                return redirect("adminlogin")
