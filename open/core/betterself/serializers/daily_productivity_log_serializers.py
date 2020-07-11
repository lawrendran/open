from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from open.core.betterself.models.daily_productivity_log import DailyProductivityLog
from open.core.betterself.serializers.mixins import BaseCreateUpdateSerializer
from open.core.betterself.serializers.validators import ModelValidatorsMixin


class DailyProductivityLogReadSerializer(ModelSerializer):
    class Meta:
        model = DailyProductivityLog
        fields = (
            "source",
            "date",
            "very_productive_time_minutes",
            "productive_time_minutes",
            "neutral_time_minutes",
            "distracting_time_minutes",
            "very_distracting_time_minutes",
            "notes",
        )


class DailyProductivityLogCreateUpdateSerializer(
    BaseCreateUpdateSerializer, ModelValidatorsMixin
):
    class Meta:
        model = DailyProductivityLog
        fields = (
            "source",
            "date",
            "very_productive_time_minutes",
            "productive_time_minutes",
            "neutral_time_minutes",
            "distracting_time_minutes",
            "very_distracting_time_minutes",
            "notes",
        )

    def validate(self, validated_data):
        user = self.context["request"].user
        is_creating_instance = not self.instance

        if is_creating_instance:
            if self.Meta.model.objects.filter(
                user=user, date=validated_data["date"],
            ).exists():
                raise ValidationError(
                    f"Fields user, ingredient, measurement, and quantity are not unique!"
                )

        return validated_data
