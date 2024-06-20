# from rest_framework import serializers
# from msauthentication.models import CustomUser

# class UpdateCustomUserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required = True,
#     )

#     class Meta:
#         model = CustomUser
#         fields = '__all__'

#     def validate_email(self, value):
#         customUser = self.context['request'].customUser

#         if CustomUser.objects.exclude(pk=customUser.pk).filter(email=value).exist():
#             raise serializers.ValidationError(
#                 {
#                     'error': 'This email is already in use'
#                 }
#             )
#         return value

#     def update(self, instance, validated_data):
#         customUser = self.context['request'].customUser

#         if customUser.pk != instance.pk:
#             raise serializers.ValidationError(
#                 {
#                     'error': 'You do not have permission for this user'
#                 }
#             )

#         instance