import dash
from dash import html, dcc, Input, Output

# Librerias del algoritmo de machine learnig
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos


# Entrenar el modelo 0
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Entrenar el modelo de clasificación
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo0 = RandomForestClassifier(random_state=42)
modelo0.fit(X_train, y_train)
y_pred = modelo0.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

modelo1 = RandomForestClassifier(random_state=42)
modelo1.fit(X_train, y_train)
y_pred = modelo1.predict(X_test)

modelo2 = RandomForestClassifier(random_state=42)
modelo2.fit(X_train, y_train)
y_pred = modelo2.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)



# Entrenar el modelo 1

# Entrenar el modelo 2

# Entrenar el modelo 3

# Definir listas

# Escualas
opciones_escuelas = [
    {'label': 'División de Ingenierías', 'value': 'IN'},
    {'label': 'División Hum. y Cs. Sociales', 'value': 'HU'},
    {'label': 'Escuela de Arquitectura, Urb. y Dis.', 'value': 'AQ'},
    {'label': 'IESE - Inst. de Estudios en Educ.', 'value': 'IE'},
    {'label': 'Escuela de Negocios', 'value': 'AD'},
    {'label': 'Div Derecho, Cs. Pol. y Rel. Int.', 'value': 'JU'},
    {'label': 'División Ciencias de la Salud', 'value': 'CS'},
    {'label': 'Música', 'value': 'VA'},
    {'label': 'División de Ciencias Básicas', 'value': 'BA'},
    {'label': 'Instituto de Idiomas', 'value': 'HU'},
    {'label': 'Instituto de Idiomas', 'value': 'II'}
]

#Programas
opciones_programas = [
    {'label': 'Ingeniería Industrial', 'value': 'PINGINDUSTRL'},
    {'label': 'Psicología', 'value': 'PRPSICOLOGIA'},
    {'label': 'Diseño Gráfico', 'value': 'PDISENOGRAFI'},
    {'label': 'Ingeniería Mecánica', 'value': 'PINGMECANICA'},
    {'label': 'Lic. en Educación Infantil', 'value': 'PLICPEDAGINF'},
    {'label': 'Economía', 'value': 'PROFECONOMIA'},
    {'label': 'Negocios Internacionales', 'value': 'PNEGINTNALES'},
    {'label': 'Derecho', 'value': 'PROFEDERECHO'},
    {'label': 'Relaciones Internacionales', 'value': 'PRELINTERNAC'},
    {'label': 'Ingeniería Civil', 'value': 'PINGENICIVIL'},
    {'label': 'Administración de Empresas', 'value': 'PADMEMPRESAS'},
    {'label': 'Contaduría Pública', 'value': 'PRCONTADURIA'},
    {'label': 'Diseño Industrial', 'value': 'PDISENOINDUS'},
    {'label': 'Música', 'value': 'PROFESMUSICA'},
    {'label': 'Medicina', 'value': 'PRMEDICINA12'},
    {'label': 'Ingeniería Electrónica', 'value': 'PINGELECTRON'},
    {'label': 'Enfermería', 'value': 'PRENFERMERIA'},
    {'label': 'Comunicación Social y Period.', 'value': 'PCOMUNSOCIAL'},
    {'label': 'Ciencia Política y Gobierno', 'value': 'PCIENPOLIGOB'},
    {'label': 'Ingeniería Eléctrica', 'value': 'PINGELECTRIC'},
    {'label': 'Odontología', 'value': 'PRODONTOLOGI'},
    {'label': 'Ingeniería de Sistemas', 'value': 'PINGSISTEMAS'},
    {'label': 'Arquitectura', 'value': 'PARQUITECTUR'},
    {'label': 'Matemáticas', 'value': 'PMATEMATICAS'},
    {'label': 'Lenguas Modernas y Cultura', 'value': 'PLENGMODCULT'},
    {'label': 'Geología', 'value': 'PROFGEOLOGIA'},
    {'label': 'Filosofía y Humanidades', 'value': 'PFILOSOHUMAN'},
    {'label': 'Ciencia de Datos', 'value': 'PRCIENCIADAT'},
]

app = dash.Dash(__name__)

# Definir el layout del dashboard
app.layout = html.Div([
    html.Div([
        html.Img(src='C:/UNINORTE/MA/MA/Logoh.png', style={'width': '100px', 'height': '100px'}),
        html.H1("Universidad ABC", style={'margin-left': '20px', 'display': 'inline-block'}),
        html.H2("Formulario de inscripción"),
    ]),
    html.Div([
        html.H3("Ingrese sus datos personales:"),
        html.Div([
            html.Label("Edad:"),
            dcc.Input(id='edad', type='number'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Sexo:"),
            dcc.Dropdown(
                id='sexo',
                options=[
                    {'label': 'Femenino', 'value': 'F'},
                    {'label': 'Masculino', 'value': 'M'}
                ]
            ),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Estrato:"),
            dcc.Dropdown(
                id='estrato',
                options=[
                    {'label': str(i), 'value': i} for i in range(1, 7)
                ]
            ),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Ciudad de bachillerato:"),
            dcc.Input(id='bach_ciudad', type='text'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Departamento de bachillerato:"),
            dcc.Input(id='bach_depto', type='text'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("País de bachillerato:"),
            dcc.Input(id='bach_pais', type='text'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Colegio privado:"),
            dcc.Dropdown(
                id='col_privado',
                options=[
                    {'label': 'Sí', 'value': 'Y'},
                    {'label': 'No', 'value': 'N'}
                ]
            ),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Código DANE del Colegio de bachillerato:"),
            dcc.Input(id='codigo_dane', type='number'),
            html.A('Click aquì para consultar código DANE de su colegio', href='https://sineb.mineducacion.gov.co/bcol/app?service=page/BuscandoColegioBasico'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Puntaje ICFES:"),
            dcc.Input(id='puntaje_icfes', type='number'),
        ], style={'margin-bottom': '20px'}),

        html.Div([
            html.Label("Puntaje en Matemáticas:"),
            dcc.Input(id='matematicas', type='number'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Puntaje en Lectura:"),
            dcc.Input(id='lectura', type='number'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Puntaje en Ciencias Sociales:"),
            dcc.Input(id='csociales', type='number'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Puntaje en Ciencias Naturales:"),
            dcc.Input(id='cnaturales', type='number'),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Puntaje en Inglés:"),
            dcc.Input(id='ingles', type='number'),
        ], style={'margin-bottom': '20px'}),
        html.Button('Enviar datos personales', id='submit_button'),
    ]),
    html.Div(id='output_div', children=[
        html.H4("Las personas con un perfil similar al de usted están estudiando carreras de nuestra escuela de:"),
        html.Div(id='prediction_output1'),
        html.P("Esperamos que nuestra sugerencia haya sido útil para usted. Para continuar con el proceso de inscripción debe seleccionar la escuela y el programa a cursar. "),
    ]),
    html.Div(id='output_div2', children=[
        html.H3("Escoger escuela y programa:"),
        html.Div([
            html.Label("Escuela:"),
            dcc.Dropdown(
                id='escuela',
                options=opciones_escuelas
            ),
        ], style={'margin-bottom': '20px'}),
        html.Div([
            html.Label("Programa:"),
            dcc.Dropdown(
                id='programa',
                options=opciones_programas
            ),
        ], style={'margin-bottom': '20px'}),
        html.Button('Enviar', id='submit_button2'),
    ]),
    html.Div(id='admission_div', children=[
        html.P("¿Quiere predecir si será admitido o no, de acuerdo con su perfil y el programa que escogió?"),
        html.Button('Quiero la predicción de admisión', id='admission_button'),
    html.Div(id='output_div3', children=[
        html.H4("Las personas con un perfil similar al de usted, están obteniendo como resultado de su proceso de admisión:"),
        html.Div(id='prediction_output2'),
    ]),
        html.P("Esta predicción es hecha por un programa, no es garantía de aceptación, dado que existen otros factores adicionales a su perfil que serán tenidos en cuenta en procesos posteriores a esta inscripción.")
    ]),
    html.Div(id='admission_output', children=[
        html.H3("Resultado de admisión:"),
        html.Div(id='admission_prediction'),
    ])
])

# Callback para actualizar la predicción del modelo1
@app.callback(
    Output('prediction_output1', 'children'),
    Input('submit_button', 'n_clicks'),
    Input('edad', 'value'),
    Input('sexo', 'value'),
    Input('estrato', 'value'),
    Input('bach_ciudad', 'value'),
    Input('bach_depto', 'value'),
    Input('bach_pais', 'value'),
    Input('col_privado', 'value'),
    Input('puntaje_icfes', 'value'),
    Input('codigo_dane', 'value'),
    Input('matematicas', 'value'),
    Input('lectura', 'value'),
    Input('csociales', 'value'),
    Input('cnaturales', 'value'),
    Input('ingles', 'value')
)

def update_prediction1(n_clicks, edad, sexo, estrato, bach_ciudad, bach_depto, bach_pais, col_privado,
                        puntaje_icfes, codigo_dane, matematicas, lectura, csociales, cnaturales, ingles):
    if n_clicks is None:
        return ''
    
    new_data0 = [[edad, sexo, estrato, bach_ciudad, bach_depto, bach_pais, col_privado,
                  puntaje_icfes, codigo_dane, matematicas, lectura, csociales, cnaturales, ingles]]
    
    prediction = modelo0.predict(new_data0)[0]
    
    new_data1 = new_data0.copy()
    new_data1.append(prediction)
    
    return f"Las personas con un perfil similar al de usted están estudiando carreras de nuestra escuela de: {prediction}"

# Callback para actualizar la predicción del modelo2
@app.callback(
    Output('prediction_output2', 'children'),
    Input('submit_button2', 'n_clicks'),
    Input('escuela', 'value'),
    Input('programa', 'value'),
    Input('prediction_output1', 'children')
)
def update_prediction2(n_clicks, escuela, programa, prediction_output1):
    if n_clicks is None:
        return ''
    
    new_data2 = new_data1.copy()
    new_data2.extend([escuela, programa])
    
    prediction = modelo2.predict(new_data2)[0]
    
    return f"Las personas con un perfil similar al de usted, están obteniendo como resultado de su proceso de admisión: {prediction}"

# Callback para mostrar el resultado de la admisión
@app.callback(
    Output('admission_prediction', 'children'),
    Input('admission_button', 'n_clicks'),
    Input('prediction_output2', 'children')
)
def show_admission_result(n_clicks, prediction_output2):
    if n_clicks is None:
        return ''
    
    return prediction_output2

# Correr la aplicación
if __name__ == '__main__':
#    app.run_server(debug=True)
