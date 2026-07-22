from apscheduler.schedulers.background import BackgroundScheduler

from agente_telegram.bot import bot_telegram
from agente_telegram.config.settings import settings
from agente_telegram.service.users_history import UserHistoryService


scheduler = BackgroundScheduler()


def job():
    user_history = UserHistoryService()

    for users in user_history.yield_inactive_users_for_processing():

        for user in users:

            print(user.id_user)

            bot_telegram.send_message(
                user.id_user,
                "Olá, não nos falamos a muito tempo, vamos conversar?"
            )

            user.notification_inactivity = True

scheduler.add_job(
    job,
    'cron',
    hour=settings.scheduler_hour,
    minute=settings.scheduler_minutes,
    day_of_week=settings.scheduler_day_week)


if __name__ == '__main__':
    job()



