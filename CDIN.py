# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 08:29:43 2020

@author: jonha
"""
import pandas as pd
import string

class CDIN:
    def dqr(data):
        #Lista de variables (features) de la de datos
        columns = pd.DataFrame(list(data.columns.values),columns=['Nombres'], index=list(data.columns.values))
        
        #Lista de tipos de datos
        data_types=pd.DataFrame(data.dtypes, columns=['Data_Types'])
        
        #Lista de datos perdidos (missing data)
        missing_values=pd.DataFrame(data.isnull().sum(),columns=['missing_values'])
        
        #Lista de los datos presentes
        present_values=pd.DataFrame(data.count(),columns=['present_values'])
        
        #Lista de valores únicos
        unique_values=pd.DataFrame(columns=['unique_values'])
        for col in list(data.columns.values):
            unique_values.loc[col]=[data[col].nunique()]
            
        #Lista de valores mínimos
        min_values = pd.DataFrame(columns=['min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col]=[data[col].min()]
            except:
                pass
            
        #Lista de valores mínimos
        max_values = pd.DataFrame(columns=['max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col]=[data[col].max()]
            except:
                pass
        #Regresar el reporte con la union de todos los dataframes
        return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values)
        
    #funciones de limpieza de datos
    
    
    #remover digitos
    def remove_digits(x):
        try:
            x=''.join(ch for ch in x if ch not in string.digits)
        except: 
            pass
        return x
    #remover espacios en blanco
    def remove_whitespace(x):
        try:
            x=''.join(x.split())
        except: 
            pass
        return x
    
    #reemplazar texto
    def replace_text(x, to_replace, replacement):
        try:
            x=x.replace(to_replace,replacement)
        except:
            pass
        return x
    
    # convertir a mayusculas
    def uppercase_text(x):
        try:
            x=x.upper()
        except:
            pass
        return x
    
    # convertir a minusculas
    def lowercase_text(x):
        try:
            x=x.lower()
        except:
            pass
        return x
    #remover signos de puntuación
    def remove_punctuation(x):
        try:
            x=''.join(ch for ch in x if ch not in string.punctuation)
        except: 
            pass
        return x
            