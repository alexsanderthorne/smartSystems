#Exemplo de Classificação Binária

import tensorflow as tf
import tensorflow.keras as keras

model = keras.models.Sequential()  # Cria uma rede neural sequencial - feed foward
model.add(keras.layers.Dense(20, activation='relu', input_shape=(20, 1))) # primeira hidden layer
model.add(keras.layers.Dense(20, activation='LeakyReLU')) # segunda hidden layer
model.add(keras.layers.Dense(1, activation= 'sigmoid')) # output layer com ativação sigmoid

#model.summary()



#Exemplo de Regressão

model = keras.models.Sequential()  # Cria uma rede neural sequencial - feed foward
model.add(keras.layers.Dense(20, activation='relu', input_shape=(20, 1))) # primeira hidden layer
model.add(keras.layers.Dense(20, activation='LeakyReLU')) # segunda hidden layer
model.add(keras.layers.Dense(1, activation= 'linear')) # output layer com ativação linear

#model.summary()


#Exemplo de Multiclassificação (não-binária - acima de duas classes)

model = keras.models.Sequential()  # Cria uma rede neural sequencial - feed foward
model.add(keras.layers.Dense(20, activation='relu', input_shape=(20, 1))) # primeira hidden layer
model.add(keras.layers.Dense(20, activation='LeakyReLU')) # segunda hidden layer
model.add(keras.layers.Dense(100, activation= 'softmax')) # output layer com ativação softmax com 10 classes

#model.summary()


# Como treinar sua rede neural no Keras

# Uma vez especificado o modelo, ele deve ser compilado com o comando model.compile() no qual deve se especificar a função custo loss, o otimizador optimizer e as métricas metrics como lista

model.compile(loss=keras.losses.categorical_crossentropy,
            optimizer=keras.optimizers.SGD(),
            metrics=[keras.metrics.Accuracy()])

model.add(keras.layers.Dense(4, activation='relu'))  # hidden layer
model.add(keras.layers.Dropout(0.2))  