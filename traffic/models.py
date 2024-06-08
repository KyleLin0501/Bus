# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class ActualFrequency(models.Model):
    driving_date = models.DateField(primary_key=True)  # The composite primary key (driving_date, Departure_time, driving_week, jurisdiction_unit, route_number, outbound_return) found, that is not supported. The first column is selected.
    departure_time = models.TimeField(db_column='Departure_time')  # Field name made lowercase.
    driving_week = models.CharField(max_length=3)
    jurisdiction_unit = models.CharField(max_length=30)
    route_number = models.CharField(max_length=5)
    outbound_return = models.CharField(max_length=1)
    driver_id = models.CharField(db_column='Driver_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vehicle_license_plate = models.ForeignKey('Bus', models.DO_NOTHING, db_column='vehicle_license_plate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actual_frequency'
        unique_together = (('driving_date', 'departure_time', 'driving_week', 'jurisdiction_unit', 'route_number', 'outbound_return'),)


class AppointmentForm(models.Model):
    appointment_form_id = models.CharField(primary_key=True, max_length=7)
    special_needs = models.IntegerField(blank=True, null=True)
    pick_up_location_x = models.FloatField(db_column='pick_up_location_X', blank=True, null=True)  # Field name made lowercase.
    pick_up_location_y = models.FloatField(db_column='pick_up_location_Y', blank=True, null=True)  # Field name made lowercase.
    drop_off_location_x = models.FloatField(db_column='drop_off_location_X', blank=True, null=True)  # Field name made lowercase.
    drop_off_location_y = models.FloatField(db_column='drop_off_location_Y', blank=True, null=True)  # Field name made lowercase.
    passenger_id = models.CharField(max_length=7, blank=True, null=True)
    driving_date = models.DateField(blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)
    driving_week = models.CharField(max_length=3, blank=True, null=True)
    jurisdiction_unit = models.CharField(max_length=30, blank=True, null=True)
    route_number = models.CharField(max_length=5, blank=True, null=True)
    outbound_return = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment_form'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bus(models.Model):
    license = models.CharField(primary_key=True, max_length=8)
    brand = models.CharField(max_length=24, blank=True, null=True)
    car_length = models.FloatField(db_column='Car_length', blank=True, null=True)  # Field name made lowercase.
    low_floor = models.IntegerField(blank=True, null=True)
    wheelchair_use = models.IntegerField(blank=True, null=True)
    number_of_seats = models.IntegerField(db_column='Number_of_seats', blank=True, null=True)  # Field name made lowercase.
    type_a_or_type_b = models.IntegerField(db_column='Type_A_or_Type_B', blank=True, null=True)  # Field name made lowercase.
    manual_gearbox = models.IntegerField(db_column='Manual_gearbox', blank=True, null=True)  # Field name made lowercase.
    displacement = models.IntegerField(blank=True, null=True)
    maximum_horsepower = models.FloatField(db_column='Maximum_horsepower', blank=True, null=True)  # Field name made lowercase.
    maximum_torque = models.FloatField(db_column='Maximum_torque', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bus'


class Dirver(models.Model):
    driver_id = models.CharField(db_column='Driver_id', primary_key=True, max_length=7)  # Field name made lowercase.
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    violation_record = models.IntegerField(blank=True, null=True)
    driver_license = models.CharField(max_length=5, blank=True, null=True)
    dirver_license_ed = models.DateField(db_column='dirver_license_ED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dirver'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dock(models.Model):
    location_x = models.FloatField(db_column='location_X', primary_key=True)  # Field name made lowercase. The composite primary key (location_X, location_Y, jurisdiction_unit, route_number, outbound_return) found, that is not supported. The first column is selected.
    location_y = models.FloatField(db_column='location_Y')  # Field name made lowercase.
    jurisdiction_unit = models.CharField(max_length=30)
    route_number = models.CharField(max_length=5)
    outbound_return = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dock'
        unique_together = (('location_x', 'location_y', 'jurisdiction_unit', 'route_number', 'outbound_return'),)


class HistoricalArrivals(models.Model):
    driving_date = models.DateField(primary_key=True)  # The composite primary key (driving_date, departure_time, driving_week, jurisdiction_unit, route_number, outbound_return, location_X, location_Y, arrival_time) found, that is not supported. The first column is selected.
    departure_time = models.TimeField()
    driving_week = models.CharField(max_length=3)
    jurisdiction_unit = models.CharField(max_length=30)
    route_number = models.CharField(max_length=5)
    outbound_return = models.CharField(max_length=1)
    location_x = models.FloatField(db_column='location_X')  # Field name made lowercase.
    location_y = models.FloatField(db_column='location_Y')  # Field name made lowercase.
    arrival_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'historical_arrivals'
        unique_together = (('driving_date', 'departure_time', 'driving_week', 'jurisdiction_unit', 'route_number', 'outbound_return', 'location_x', 'location_y', 'arrival_time'),)


class Passenger(models.Model):
    passenger_id = models.CharField(primary_key=True, max_length=7)
    passenger_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    mail = models.CharField(max_length=20, blank=True, null=True)
    disability_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger'


class Route(models.Model):
    jurisdiction_unit = models.CharField(primary_key=True, max_length=30)  # The composite primary key (jurisdiction_unit, route_number, outbound_return) found, that is not supported. The first column is selected.
    route_number = models.CharField(max_length=5)
    outbound_return = models.CharField(max_length=1)
    starting_point_x = models.FloatField(db_column='starting_point_X', blank=True, null=True)  # Field name made lowercase.
    starting_point_y = models.FloatField(blank=True, null=True)
    destination_x = models.FloatField(blank=True, null=True)
    destination_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'
        unique_together = (('jurisdiction_unit', 'route_number', 'outbound_return'),)


class Schedules(models.Model):
    departure_time = models.TimeField(primary_key=True)  # The composite primary key (departure_time, driving_week, jurisdiction_unit, route_number, outbound_return) found, that is not supported. The first column is selected.
    driving_week = models.CharField(max_length=3)
    jurisdiction_unit = models.CharField(max_length=30)
    route_number = models.CharField(max_length=5)
    outbound_return = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'schedules'
        unique_together = (('departure_time', 'driving_week', 'jurisdiction_unit', 'route_number', 'outbound_return'),)


class Station(models.Model):
    location_x = models.FloatField(db_column='location_X', primary_key=True)  # Field name made lowercase. The composite primary key (location_X, location_Y) found, that is not supported. The first column is selected.
    location_y = models.FloatField(db_column='location_Y')  # Field name made lowercase.
    station_name = models.CharField(max_length=50, blank=True, null=True)
    road_name = models.CharField(max_length=50, blank=True, null=True)
    accessibility = models.IntegerField(blank=True, null=True)
    waiting_area_seat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'
        unique_together = (('location_x', 'location_y'),)


class VehicleMaintenanceRecords(models.Model):
    maintenance_date = models.DateField(primary_key=True)  # The composite primary key (maintenance_date, license) found, that is not supported. The first column is selected.
    shop = models.CharField(max_length=40, blank=True, null=True)
    maintenanceg_level = models.IntegerField(blank=True, null=True)
    personnel = models.CharField(max_length=16, blank=True, null=True)
    license = models.ForeignKey(Bus, models.DO_NOTHING, db_column='license')

    class Meta:
        managed = False
        db_table = 'vehicle_maintenance_records'
        unique_together = (('maintenance_date', 'license'),)
