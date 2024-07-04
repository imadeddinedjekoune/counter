from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
from .counter import CounterThread

# Initialize and start the counter thread
counter_thread = CounterThread()
counter_thread.start()

def hello_world(request):
	current_count = counter_thread.counter
	return render(request, 'worker/worker.html', {'counter': current_count})


def counter_value(request):
    current_count = counter_thread.counter
    return JsonResponse({'counter': current_count})