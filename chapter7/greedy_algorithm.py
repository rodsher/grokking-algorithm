states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "са", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_states = set()

while states_needed:
    best_state = None
    state_covered = set()
    for state, states in stations.items():
        covered = states & states_needed
        if len(covered) > len(state_covered):
            best_state = state
            state_covered = covered

    states_needed -= state_covered
    final_states.add(best_state)

print(final_states)
            
