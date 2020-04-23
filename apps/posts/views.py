from django.shortcuts import render

# Create your views here.


def view_all_posts(request):

    context = {
        'posts': [{
            "img": "drawing1-1024x1024.jpg",
            "title": "Rain Clouds",
            "story": "Let the stormy clouds chase everyone from the place Come on with the rain, I've a smile on my face I walk down the lane with a happy refrain",

        },
            {
            "img": "drawing2-1024x1024.jpg",
            "title": "Rain Clouds",
            "story": "Let the stormy clouds chase everyone from the place Come on with the rain, I've a smile on my face I walk down the lane with a happy refrain",

        },
            {
            "img": "drawing3-1024x1024.jpg",
            "title": "Rain Clouds",
            "story": "Let the stormy clouds chase everyone from the place Come on with the rain, I've a smile on my face I walk down the lane with a happy refrain",

        },
            {
            "img": "drawing4-1024x1024.jpg",
            "title": "Rain Clouds",
            "story": "Let the stormy clouds chase everyone from the place Come on with the rain, I've a smile on my face I walk down the lane with a happy refrain",

        },
            {
            "img": "drawing5-1024x1024.jpg",
            "title": "Rain Clouds",
            "story": "Let the stormy clouds chase everyone from the place Come on with the rain, I've a smile on my face I walk down the lane with a happy refrain",

        },
            {
            "img": "drawing6-1024x1024.jpg",
            "title": "Rain Clouds",
            "story": "Let the stormy clouds chase everyone from the place Come on with the rain, I've a smile on my face I walk down the lane with a happy refrain",

        },

            {
            "img": "drawing7-1024x1024.jpg",
            "title": "There be demons",
            "story": "Let the stormy clouds chase everyone from the place Come on with the rain, I've a smile on my face I walk down the lane with a happy refrain",

        }]
    }

    return render(request, 'posts/view_all_posts.html', context)
