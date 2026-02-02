# main_modelo.py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from data_cleaner import limpiar_datos
from data_transformer import transformar_datos
from config import COLS_FEATURES
import seaborn as sns
import matplotlib.pyplot as plt

def ejecutar_modelo():
    # 1. Obtener y preparar datos (Pasos previos)
    df_limpio = limpiar_datos()
    df_final, _ = transformar_datos(df_limpio)
    
    X = df_final[COLS_FEATURES]
    y = df_final['target']
    
    # 2. Dividir en Entrenamiento y Test (80% / 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Entrenar el Modelo (Ejercicio 6)
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)
    
    print("\n--- EJERCICIO 6: RESULTADOS DEL MODELO ---")
    print(f"Precisión en entrenamiento: {modelo.score(X_train, y_train):.2f}")
    
    # 4. Evaluación (Ejercicio 8)
    y_pred = modelo.predict(X_test)
    print("\nMatriz de Confusión:")
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicción')
    plt.ylabel('Realidad')
    plt.title('Matriz de Confusión - Victoria RLCS')
    plt.show()

    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    ejecutar_modelo()