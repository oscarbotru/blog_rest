from rest_framework import serializers


class RudeWordValidator:
    def __call__(self, value):
        if value in ['badword', 'anotherbadword', 'youthinkiwilluserudeword']:
            raise serializers.ValidationError("Нельзя использовать грубые слова и оскорбления.")

        if value in ['продам', 'куплю', 'крипта', 'трейдинг', '', '', '', '']:
            raise serializers.ValidationError("Нельзя заниматься продажей в комментариях.")
