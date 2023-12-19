from deepClassifier.entity.config_entity import PrepareBaseModelConfig
from pathlib import Path
import tensorflow as tf

class PrepareBaseModel:
    def __init__(self, config:PrepareBaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.vgg16.VGG16(
            include_top = self.params.INCLUDE_TOP,
            weights = self.parmas.WEIGHTS,
            input_shape = self.params.INPUT_SHAPE
        )
        self.save_model(path = self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_model(model, freeze_all, freeze_till, classes, learning_rate):
        if freeze_all:
            model.trainable = False
        
        elif (freeze_till is not None) and (freeze_till>0):
            for layer in model.layers[:freeze_till]:
                layer.trainable=False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation = 'softmax'
        )(flatten_in)

        full_model = tf.keras.model(
            inputs = model.input,
            outputs = prediction
        )
        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
        )
        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_model(
            model = self.model,
            classes= self.params.CLASSES,
            freeze_all= True,
            freeze_till= None,
            learning_rate= self.params.LEARNING_RATE
        )
        self.full_model.save_model(path = self.config.updated_model_path, model = self.model)

        
    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)
    







        



        
    

