def public_service(times):
    public_service_man_sorted_time = sorted(times)
    total_wait = 0
    service_wait = 0
    for tm in public_service_man_sorted_time:
        total_wait += service_wait
        service_wait += tm
    return total_wait

times = [7, 2, 9]
time_waiting = public_service(times)
print("Time to wait: ", time_waiting)