var timeFunction = setInterval(checkPageLoaded, 3000);

function checkPageLoaded () {
	var challengeTitle = document.getElementsByClassName("dynamic-header-center")[0].innerHTML;
	if (challengeTitle != "Submission") {
		clearInterval(timeFunction);
		logData(challengeTitle, window.location.href);
	}
}

function logData(challengeName, address) {
	$.post("https://5000-f051d1ab-5e83-4fd2-b736-7eec60fac759.ws-eu01.gitpod.io/add_data",
    {
      name: challengeName,
      url: address
    },
    function(data,status){
      alert("Data: " + data + "\nStatus: " + status);
    });
}