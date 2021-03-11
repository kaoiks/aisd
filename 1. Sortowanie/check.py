# Sprawdza czy tablica jest posortowana. Zwraca krotkę (czy posortowany, opis)
def check_sort(arr):
    is_asc = True
    is_desc = True

    for i in range(1, len(arr)):
        if not is_asc and not is_desc:
            break
        
        if arr[i] > arr[i-1]:
            is_desc = False
        if arr[i] < arr[i-1]:
            is_asc = False
    
    if is_asc and is_desc:
        return (True, "Ciąg posortowany - stały")
    if is_asc:
        return (True, "Ciąg posortowany - niemalejąco")
    if is_desc:
        return (True, "Ciąg posortowany - nierosnąco")
    return (False, "Ciąg nie jest posortowany")