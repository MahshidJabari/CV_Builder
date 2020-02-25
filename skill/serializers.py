from rest_framework import serializers
from skill.models import Skill, Skills, Honors, Language, AcademicCertificate


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('name', "level")


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', "readingLevel", "writingLevel", "listeningLevel", "speakingLevel")


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCertificate
        fields = ('type', "title", "institute", "year", "month")


class HonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honors
        fields = ("title", "year", "month")


class SkillSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True, write_only=True)
    language = LanguageSerializer(many=True, write_only=True)
    certificate = CertificateSerializer(many=True, write_only=True)
    honor = HonorSerializer(many=True, write_only=True)

    class Meta:
        model = Skill
        fields = ('cv_id', "skills", "language", "certificate", "honor")
