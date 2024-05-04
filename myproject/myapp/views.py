from django.shortcuts import render
from .forms import InputForm
from .my_python_programm import create_plot  # Импорт функции из внешнего файла

def my_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            plot_url = create_plot(form.cleaned_data['user_input'])
            # Передача URL для изображения в контекст шаблона
            context = {'form': form, 'plot_url': plot_url}
            return render(request, 'myapp/result.html', context)
    else:
        form = InputForm()

    # Отображение пустой формы при первом заходе на страницу
    return render(request, 'myapp/index.html', {'form': form})
