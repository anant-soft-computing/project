from core.models import Event, EventRegistration, Registration


def main():
    for i in Registration.objects.all():
        print(i.id)
        for j in Event.objects.all():
            print(j.event_name)
            if not EventRegistration.objects.filter(event=j, registration=i).exists():
                event_obj = EventRegistration()
                event_obj.event = j
                event_obj.registration = i
                event_obj.save()

    print("Done")


# from script import main
if __name__ == "__main__":
    main()
