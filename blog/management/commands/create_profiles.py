from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Profile
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Creates profiles for users that do not have one'

    def handle(self, *args, **options):
        users_without_profile = []
        for user in User.objects.all():
            try:
                # Try to access the user's profile
                profile = user.profile
                self.stdout.write(f"User {user.username} already has a profile")
            except ObjectDoesNotExist:
                # If the profile doesn't exist, create one
                users_without_profile.append(user)
                try:
                    profile = Profile.objects.create(user=user)
                    self.stdout.write(f"Created profile for {user.username}")
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error creating profile for {user.username}: {str(e)}"))
        
        if users_without_profile:
            self.stdout.write(self.style.SUCCESS(f'Created profiles for {len(users_without_profile)} users'))
        else:
            self.stdout.write(self.style.SUCCESS('All users already have profiles')) 