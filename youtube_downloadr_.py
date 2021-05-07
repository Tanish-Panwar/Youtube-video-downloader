# We just imported the webbrowser module(library)
import webbrowser
# then we set url as input which takes the url
url = input("Enter Video Url:\n")
# the we said open url with webbrowser
url = url[:12]+"ss"+url[12:]
webbrowser.open(url)




