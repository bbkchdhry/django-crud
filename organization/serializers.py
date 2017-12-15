from rest_framework import serializers
from organization.models import Organization, Department


class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Department
        fields = ('id', 'dept_name')


class OrganizationSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('id', 'org_name', 'org_type', 'departments')

    def create(self, validated_data):
        departments = validated_data.pop('departments')
        organization = Organization.objects.create(**validated_data)
        print('org: ', organization)
        for dept in departments:
            print('dept: ', dept)
            Department.objects.create(organization=organization, **dept)
        return organization

    def update(self, instance, validated_data):
        departments_data = validated_data.pop('departments')

        instance.org_name = validated_data.get('org_name', instance.org_name)
        instance.org_type = validated_data.get('org_type', instance.org_type)
        instance.save()

        for dept in departments_data:
            Department.objects.filter(id=dept.get('id')).update(dept_name=dept.get('dept_name'))

        return instance

