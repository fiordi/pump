from django.db import models

"""
PacketState Class (Interface)
"""
class PacketState(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, unique=True, default='Undefined')

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'

"""
PacketActivated Class (Singleton)
"""
class PacketActivated(PacketState):

    def setName(self):
        self.name = "Activated"
        self.save()

"""
PacketDeativated Class (Singleton)
"""
class PacketDeactivated(PacketState):

    def setName(self):
        self.name = "Deactivated"
        self.save()


"""
PacketIncomplete Class (Singleton)
"""
class PacketIncomplete(PacketState):

    def setName(self):
        self.name = "Incomplete"
        self.save()