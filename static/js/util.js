function switch_chk() {
    document.getElementsByName('checked').forEach(item => {item.checked = this.checked;});
    this.indeterminate = false;
}
function chk_switched() {
    let qty_all = document.getElementsByName('checked').length;
    let qty_chk = document.querySelectorAll('input[name="checked"]:checked').length;
    let sc = document.getElementById('switch_checked');
    sc.checked = (qty_chk > 0);
    sc.indeterminate = (qty_chk !== qty_all);
}
