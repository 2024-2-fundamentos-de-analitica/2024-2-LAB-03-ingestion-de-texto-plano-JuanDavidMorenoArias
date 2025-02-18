"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


      
      
    
    df = pd.read_csv('../files/input/clusters_report.txt', sep='\s{2,}', skiprows=3)
    return df
    """
    with open('files/input/clusters_report.txt', 'r') as f:
       lines = f.readlines()

    # Remove header and separator lines
    lines = lines[4:]  # Skip the first 3 lines (headers and separator)

    # Prepare data to split into columns using regex
    data = []
    dataf = []
    #return lines[4].split()
    #print(lines[0].split())

    palabras_clave = ''
    for i in lines:
        line = i.split()
        
        
        #print(line[0].isdigit())
        if len(line) < 1:
            pass
        elif line[0].isdigit():
            if len(palabras_clave) > 0:
              data.append([word.strip('.') for word in palabras_clave.split(', ')])
              dataf.append(data)
              palabras_clave = ''
              data = []

            data.append(int(line[0]))
            data.append(int(line[1]))
            data.append(float(line[2].replace(',', '.')))
                

            # Join the rest of the line into the keywords string
            
            palabras_clave = ' '.join(line[4:])

        else:
            palabras_clave += ' ' + ' '.join(line)
    
    if len(palabras_clave) > 0:
        data.append([word.strip('.') for word in palabras_clave.split(', ')])
        dataf.append(data)
              

    # Create the dataframe
    df = pd.DataFrame(dataf, columns=["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"] )
    df["principales_palabras_clave"] = df["principales_palabras_clave"].apply(lambda x: ", ".join(x))

    return df


# Example usage
if __name__ == '__main__':
    print(pregunta_01())