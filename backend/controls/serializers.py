from rest_framework import serializers
from .models import Framework, Control
from core.serializers import RiskSerializer  # import RiskSerializer to nest if needed

class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = '__all__'

class ControlSerializer(serializers.ModelSerializer):
    # Show related risks as IDs or nested objects
    risks = serializers.PrimaryKeyRelatedField(many=True, queryset=None)  # assigned in __init__

    class Meta:
        model = Control
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['risks'].queryset = self.context['request'].user.core_risk_set.all() if self.context.get('request') else None
