/* Langar One — form handling.
 *
 * To send submissions to a Google Form (and its response Sheet):
 *   1. Set `action` to the form's ".../formResponse" URL.
 *   2. Set each field to that question's "entry.123456789" id.
 * A form with `emailTo` set emails each submission to that address through FormSubmit.
 * With neither set, the form opens a pre-filled email to info@langar.one instead.
 */
var LANGAR_FORMS = {
  volunteer: {
    action: "",
    /* Emails each submission through FormSubmit (formsubmit.co). Leave empty to fall back to the visitor's email app. */
    emailTo: "ricky@langar.one",
    subject: "Volunteer application",
    fields: { firstName: "", lastName: "", email: "", phone: "", cityState: "" }
  },
  event: {
    action: "",
    subject: "Event proposal",
    fields: { name: "", email: "", phone: "", organization: "", eventType: "", location: "" }
  }
};
var LANGAR_EMAIL = "info@langar.one";

document.querySelectorAll("form[data-form]").forEach(function (form) {
  var cfg = LANGAR_FORMS[form.dataset.form];
  var msg = form.querySelector(".form-msg");
  var button = form.querySelector("button[type=submit]");

  function show(text) {
    msg.textContent = text;
    msg.hidden = false;
    msg.focus();
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var inputs = form.querySelectorAll("[name]");

    if (cfg.action) {
      var data = new FormData();
      inputs.forEach(function (el) {
        var id = cfg.fields[el.name];
        if (id) data.append(id, el.value);
      });
      button.disabled = true;
      fetch(cfg.action, { method: "POST", mode: "no-cors", body: data })
        .then(function () {
          form.reset();
          show("Thank you! We've received your details and will be in touch.");
        })
        .catch(function () {
          show("Something went wrong sending the form. Please email us at " + LANGAR_EMAIL + ".");
        })
        .then(function () { button.disabled = false; });
      return;
    }

    if (cfg.emailTo) {
      var payload = { _subject: "Langar One: " + cfg.subject, _template: "table", _captcha: "false" };
      inputs.forEach(function (el) {
        if (el.name === "_honey") { payload._honey = el.value; return; }
        if (el.value) payload[el.name === "email" ? "email" : el.dataset.label] = el.value;
      });
      var failed = "We couldn't send the form just now. Please email us at " + LANGAR_EMAIL + " and we'll get back to you.";
      button.disabled = true;
      fetch("https://formsubmit.co/ajax/" + cfg.emailTo, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload)
      })
        .then(function (r) { return r.json(); })
        .then(function (res) {
          if (String(res.success) === "true") {
            form.reset();
            show("Thank you! We've received your application and will be in touch by email.");
          } else {
            show(failed);
          }
        })
        .catch(function () { show(failed); })
        .then(function () { button.disabled = false; });
      return;
    }

    var lines = [];
    inputs.forEach(function (el) {
      if (el.value && el.name !== "_honey") lines.push(el.dataset.label + ": " + el.value);
    });
    window.location.href = "mailto:" + LANGAR_EMAIL +
      "?subject=" + encodeURIComponent(cfg.subject) +
      "&body=" + encodeURIComponent(lines.join("\n"));
    show("Your email app should open with your details filled in. Press send to finish. If nothing opens, email us at " + LANGAR_EMAIL + ".");
  });
});
