from django.shortcuts import render
from Ventas.models import Venta
import plotly.express as px
import pandas as pd

def ventaControlador(request):
    ventas = Venta.objects.all()

    df = pd.DataFrame(ventas.values())

    # Calcular el promedio de ventas por mes en cada barrio
    promedio_ventas = df.groupby(['Barrio', 'Mes']).size().reset_index(name='Ventas')
    promedio_ventas = promedio_ventas.groupby(['Barrio', 'Mes'])['Ventas'].mean().reset_index()

    fig = px.pie(promedio_ventas, values='Ventas', names='Mes', hole=.3,
                 title="Ventas Realizadas por mes")

    fig3 = px.scatter_matrix(promedio_ventas, dimensions=["Ventas", "Mes"], color="Barrio")
    
    fig.update_layout(title_font_family="Comic Sans")
    fig3.update_layout(title_font_family="Comic Sans")
    
    mihtml2 = fig.to_html(full_html=False)
    mihtml4 = fig3.to_html(full_html=False)

    context = {
        "nombre": "Angel",
        "ventas": ventas,
        "fig": mihtml2,
        "fig3": mihtml4
    }
    return render(request, "Ventas/index.html", context)




