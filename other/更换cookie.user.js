// ==UserScript==
// @name         twitter更换cookie
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  切换浏览器cookie
// @author       二次蓝
// @match        https://twitter.com/*
// @match        https://twitter.com/home?lang=en
// @match        https://twitter.com/account/access
// @icon         data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAG9klEQVR4nO1aCWwVVRQ9LXvRqog7KLaCghFUVOK+gFvExKqAC8W1VasiuAQViKJGwYgEULGCQQREC9pEEJBFFgURN8RQoeyiRBQqAmKxtDU3OdNcH7O8P/3zW5I5ycv/M/OW+97ce9+95w0QI0aMGDFixIgRLY4GcAuAVwDMArAGwHYA+1i2894s1pG6R+EgRwsAfQF8A6AKQHWCpRLAcgAPATgCBxFOBPA6gHI1Gfk/D8AgADkA2gNoCaAJS0veuxHAYADzqRlO+38AvAagFeoxMgAMU4LLW18IoDeA5iH6kza5ABYpDZKFfIlj1StcBmCjmvjHAM5OYv/nAJihNGIDgMtRD5BOld1PwdZwMaJCNwBrOZaMOZAy1AkaA5ii3spoAE3V88MjGrcZgDfUuO9TlpSiGYC5FGAvty2NEXy2FMBJEclwO52jjDMnlX6hEYBPOPBOAJe41PlDvSH5f0VEsoi5/cVxZlC2yDGeA+4GcJ5HnYHGnl4BoH9E8nShLDLO24gY93Mg2eq6BtTNpXnohZhE80k2rgTwL8fIR0TooIIbic5s0BnAZmMRvovILzyigqbTk915Oh2aDFCUYFuJ6RcYi7ANQGuP+p97hMZyPwgfsu6SZG+Pd7Pj7UxswIjsPQBpFu0bAhhpTEhMJJEFWGwxzrEAylhfZE4KmgDYZNjXtbzexee2yOWu8DXj/yhQQNk2JSs+uIcdruU204yhqNx71Kfd8QBGUf3fAtAugTFPZZsF7EP6soXIuJ7y5SEJ+Jad3cvrB3i9gqrthlZGLCDlbwAdLcbrxLq6rfR1QgIy57OdpOK1QicV8Eh21gDAOt67yafdGA87nm4xphNkmUVSbFscogIkmUNoDGIn43h9Fa9LA7zsEo9JbLEYc4tHW+kzTMAmcwiNL9iJEBWCN3n9bEC7iR6TEJsOwiKPtu8mKPvNbCdzCIUGAPawE6G3BD9bqlVHg9FxeAKJ2IJwtQuFJn2dkaD8RyrfEyomaMcOZNLgIjg5QJpljD6fQc8STswW1zDw2kYqzSvnsDWntmEaX2qo7QW8XoaDBwspcyj2qBcbFysNmOmS+4O5uKS851P9s8jkppyoMFDMOdyQaMOuAHaw8VSL+qM9HFc1s7QyBicrAXxJMqWInlrY3qEABjDJugtAD9JftV3QIsowwtJsa0LJCjWBTxGMYaxbxkmu538nRU1m0Qv6UYCDm2NQZ4Hs9IvKY3/A/6vU82V0bOZqOrnBRpdnjWk+96n9vBvf8p186wOoBaWqzlxqy0qG3m4LWhHAL5SwnpPG/0BtckV31WlvJjkVZF8zjG1QaGoNIUN/4zM3ikxwMZ9vZqh6ocuJj43NNla5v+wQXsig7OU0o5/YZiuAbLcGn7GCvA0zopPFEbxqZIUaT/HZcg9blbzhKxeV/pVvexSFk3vn+kxM+lnNen186l1vBEKZalcQLT4Au/jQyffBxXCoLMFhdFJutpSpssSpHrR4c/qYd5gSO4GWLvMYhHlhMOut9knGQK5C6j2u7rVQOcIBsYEjjD6VPY52J6UN7CiwnexHFnQyF+xkDy+cxmfXUa17+jC7ZwEYS/9UyWDJC20o8z7OQWO6Ed7XwFGPx/B/jON9OQSxwZlMQ803u5cp9DRum88AeJDxRg+WHP7mUY6XAcwG8Ivh+JzU3AtTjCTOzdQds65BjiIVC0gvSQ5eqAaXBMMW4iif4DmhY9u1KaJZEywIz56sv8eFSOlAxyiLeIxb4+Eeg1epTkXNwyCTbUXAhwEM4RFXkUsp5IcST/PFtA3wCw46K1OuIi+Rza2yu6L23DSjBjk0h9300NOYiY1UxKgkOvUNXVT0utglG3WKkK6HhhkgnbuBowkSK9QX5Ko3P4nacgp5iQ30P3Ie0a+2x2eNDHp7souXTSVaGyfUYyxNpda4Ta247KsvpHghhFJ/Xh297fE5Z4gMWeqrkGranNBWF0X0FtIZTk80vj8qtoxRko40RX3PNjLIHcy+7uDHT2HsriG3vD6M6jTN7gRD+xVdl3K0pzASpIAm8KT6hMVMYUu4oxQy8xvE6K8fg6Lh3J4kxf3ew4uXsF2W+kDj1rpagDyVZ7ud7ORRXb1obptSSrMqcCFF+4dki5OGCZZH5UNYbwXptL50YEN52CFszXNMWvLVLrPO+ObIxGmst62uPpRaRQH8PofLZmhdxfzfBuIvfmTfkvlFxvrWFk7q68fXO5mXpL+JMtJV3OYkfveCswv51YkM4zn4TJeDy0yeHsnzP70SjwCMVQxOLyN8zVS8wNZUBT8m5DOX3wOcWBWDpjBoSkLWr/9Kps91hmx+luKwLE4pJ6F5QM6dINKZ+y81xijnPT9SJEaMGDFixIgRA374DwxG0VHAate/AAAAAElFTkSuQmCC
// @grant        GM_registerMenuCommand
// @grant        GM_setValue
// @grant        GM_getValue
// ==/UserScript==

(function() {
    'use strict';
    // 需要更换的account、auth_token
    const text = `account1;108dedf370b0031a742e59b87042f6c9551aaaaa
account2;7e61adf31b2c73507ddc774bf4eef43456111111
`;

    var initialState;

    let id = GM_registerMenuCommand ("编辑cookie列表", function(){
        alert('未实现orz');
        // GM_unregisterMenuCommand(id);//删除菜单
    }, "h");

    function getInitialState() {
        if (initialState !== undefined) {
            return initialState;
        }
        var scriptTags = document.getElementsByTagName('script');
        var initialStateScript = null;

        for (var i = 0; i < scriptTags.length; i++) {
            var script = scriptTags[i];
            if (script.innerHTML.includes('window.__INITIAL_STATE__')) {
                initialStateScript = script;
                break;
            }
        }

        if (initialStateScript) {
            var regex = /window\.__INITIAL_STATE__=(.*?);window.__META_DATA__/;
            var match = initialStateScript.innerHTML.match(regex);

            if (match && match[1]) {
                var json = match[1];
                var data = JSON.parse(json);

                console.log(data);
                initialState = data;
                return data;
            }
        }
    }
    function getCurAccounr() {
        if (document.location.href === "https://twitter.com/account/access") {
            return document.querySelector("body > div.PageContainer > div > div.UserHeader > div > span").innerText.substring(1);
        }
        let initialState = getInitialState();
        return initialState.settings.remote.settings.screen_name;
    }

    var needLoginData = [];

    var lines = text.split("\n");
    for (var i = 0; i < lines.length; i++) {
        var line = lines[i].trim();
        if (!line) {
            continue;
        }
        var values = line.split(";");

        var account = values[0].trim();
        var ck = values[1].trim();
        console.log(i+1, "Account:", account, ck);
        needLoginData.push({"account": account, "cookie": ck});
    }


    function checkIsInlist(account) {
        for (var i = 0; i < needLoginData.length; i++) {
            let data = needLoginData[i];
            if (data.account === account) {
                return true;
            }
        }
        return false;
    }

    function defaultListener() {
        alert('clicked!');
    }
    function login(index) {
        console.log("登录" + index, needLoginData[index].account);

        /*
            var cookies = document.cookie.split(";");

            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i];
                var eqPos = cookie.indexOf("=");
                var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            }*/
        console.log("document.cookie = \"auth_token=" + needLoginData[index].cookie + "; expires=Thu, 01 Jan 2099 00:00:00 UTC; path=/\"");
        document.cookie = "auth_token=" + needLoginData[index].cookie + "; expires=Thu, 01 Jan 2099 00:00:00 UTC; path=/";
        document.location.reload();
    }

    function LoginPreListener() {
        var curAccountIndex = GM_getValue('curAccountIndex');
        if (curAccountIndex === undefined || !isListAcount) {
            GM_setValue('curAccountIndex', 0);
            login(0);
        } else {
            var newIndex = curAccountIndex - 1;
            if (newIndex < 0) {
                return;
            }
            GM_setValue('curAccountIndex', newIndex);
            login(newIndex);
        }
    }
    function LoginNextListener() {
        var curAccountIndex = GM_getValue('curAccountIndex');
        if (curAccountIndex === undefined || !isListAcount) {
            GM_setValue('curAccountIndex', 0);
            login(0);
        } else {
            var newIndex = curAccountIndex + 1;
            GM_setValue('curAccountIndex', newIndex);
            login(newIndex);
        }
    }

    var curLoginedAccount = getCurAccounr();
    console.log("curLoginedAccount", curLoginedAccount);
    var isListAcount = checkIsInlist(curLoginedAccount);
    var curAccountIndex = GM_getValue('curAccountIndex');
    console.log("curAccountIndex", curAccountIndex);

    function createBall(bottom, textContent, listener) {
        var ball = document.createElement('div');
        ball.style.cssText = `
    position: fixed;
    bottom: ` + bottom + `px;
    right: 30px;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background-color: rgb(29, 155, 240);
    cursor: pointer;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-weight: 800;
    color: white;
`;
        ball.textContent = textContent;
        ball.addEventListener('click', listener);
        document.body.appendChild(ball);
    }

    if (curAccountIndex > 0 && isListAcount) {
        createBall(120, '上一个', LoginPreListener);
    }


    if (curAccountIndex === undefined || curAccountIndex < needLoginData.length - 1 || !isListAcount) {
        var textContent;
        if (isListAcount) {
            textContent = '下一个\n' + (curAccountIndex + 1) + "/" + needLoginData.length;
        } else {
            textContent = '登录';
        }
        createBall(30, textContent, LoginNextListener);
    } else {
        createBall(30, '没有下一个\n' + (curAccountIndex + 1) + "/" + needLoginData.length, defaultListener);
    }
})();