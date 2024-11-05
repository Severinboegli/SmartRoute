function deleteProduct(element) {
    if(window.confirm("Wollen Sie das Item wirklich löschen"))
    {
        element.parentElement.submit();
    }
}

function deleteCustomer(element) {
    if(window.confirm("Wollen Sie den Kunden wirklich löschen?"))
    {
        element.parentElement.submit();
    }
}

