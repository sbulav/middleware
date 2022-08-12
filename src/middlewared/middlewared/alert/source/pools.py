from middlewared.alert.base import AlertClass, AlertCategory, AlertLevel, Alert, AlertSource
from middlewared.alert.schedule import CrontabSchedule


class PoolUSBDisksAlertClass(AlertClass):
    category = AlertCategory.STORAGE
    level = AlertLevel.WARNING
    title = 'Pool consuming USB disks'
    text = '%(pool)r is consuming %(disks)r USB disk(s) which is not advised behavior. ' \
           'Please replace the disk(s) immediately.'


class PoolDisksChecksAlertSource(AlertSource):
    schedule = CrontabSchedule(hour=0)  # every 24 hours
    run_on_backup_node = False

    async def check(self):
        alerts = []

        for pool in await self.middleware.call('pool.query'):
            usb_disks = await self.middleware.call('pool.get_usb_disks', pool['id'])
            if usb_disks:
                alerts.append(Alert(
                    PoolDisksChecksAlertSource,
                    {'pool': pool['name'], 'disks': usb_disks},
                ))

        return alerts
