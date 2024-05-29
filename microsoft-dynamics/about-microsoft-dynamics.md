# About Microsoft Dynamics 

## Use case 

When a user signs up or changes their data on a platform, I need to make an API call to a Microsoft Dynamics endpoint to sync the user data to the data in the Microsoft Dynamics CRM stays consistent with the database that powers the website. 

I've never used MS Dynamics, and I wanted to document how I learned what to do. 

## Links 

### [Dynamics 365 REST APIs | Microsoft Learn](https://learn.microsoft.com/en-us/rest/dynamics365/)

> Dynamics 365 unifies the capabilities of CRM business software and ERP systems by providing intelligent applications that seamlessly work together in the cloud. For more information, see [Dynamics 365 documentation](https://learn.microsoft.com/en-us/dynamics365/).

<img width="1717" alt="Screenshot 2024-05-29 at 9 49 25 AM" src="https://github.com/williln/til/assets/2286304/20d23c9a-bad1-4fae-8526-664feec99cc4">


This page wasn't useful, other than pointing to the Dynamics 365 docs: 

---

### [Dynamics 365 documentation | Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/)

<img width="1728" alt="Screenshot 2024-05-29 at 9 50 09 AM" src="https://github.com/williln/til/assets/2286304/9204fde2-1a98-47d6-a4f5-eb06c876aa47">

This page looks more promising, but I'm not sure what I'm looking for.  

---

The first link also contained a link to the Customer Engagement docs: 

### [Dynamics 365 Customer Engagement REST APIs | Microsoft Learn](https://learn.microsoft.com/en-us/rest/dynamics365/customer-engagement/)

<img width="1726" alt="Screenshot 2024-05-29 at 9 51 39 AM" src="https://github.com/williln/til/assets/2286304/db8954b0-4b49-4a07-84d6-e36ec627aeaa">

This page contained a link to the [Use the Microsoft Dynamics 365 Web API](https://learn.microsoft.com/en-us/previous-versions/dynamicscrm-2016/developers-guide/mt593051(v=crm.8)?redirectedfrom=MSDN), which contained a purple notice that it was out-of-date. None of the prior pages that linked to it, so far, contained that notice. 
<img width="1728" alt="Screenshot 2024-05-29 at 9 52 35 AM" src="https://github.com/williln/til/assets/2286304/beec503c-5871-44ab-aeaf-3b2659e27973">

Now, I wonder if I am in the right place, if this is the API I need after all. 


--- 

Back to [Dynamics 365 documentation](https://learn.microsoft.com/en-us/dynamics365/): 

I followed a link to get here: [Use the Microsoft Dataverse Web API (Dataverse) - Power Apps | Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview) 

<img width="1728" alt="Screenshot 2024-05-29 at 9 57 23 AM" src="https://github.com/williln/til/assets/2286304/a2e16d99-ec53-4e28-8bfa-bd0c6f15a7be">

> The Dataverse Web API provides a development experience that can be used across a wide variety of programming languages, platforms, and devices. The Web API implements the OData (Open Data Protocol), version 4.0, an OASIS standard for building and consuming RESTful APIs over rich data sources. You can learn more about this protocol at https://www.odata.org/. Details about this standard are available at https://www.oasis-open.org/standards#odatav4.0.

I was really hoping this was not the case, and I don't think it is, because I followed more links, and finally got here: 

---

### [Use OAuth authentication with Microsoft Dataverse (Dataverse) - Power Apps | Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth)

- [Example demonstrating a delegating message handler](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth#example-demonstrating-a-delegating-message-handler):

> The recommended approach is to implement a class derived from DelegatingHandler which will be passed to the constructor of the HttpClient. This handler will allow you to override the HttpClient.SendAsync method so that the access token will be refreshed by the AcquireToken* method calls with each request sent by the Http client.

Their example is in C#. There is more to it than this -- see the link -- but I wanted to include a snippet: 

```
class OAuthMessageHandler : DelegatingHandler
{
    private AuthenticationHeaderValue authHeader;
    public OAuthMessageHandler(string serviceUrl, string clientId, string redirectUrl, string username, string password,
            HttpMessageHandler innerHandler)
        : base(innerHandler)
    {
        string apiVersion = "9.2";
        string webApiUrl = $"{serviceUrl}/api/data/v{apiVersion}/";
        var authBuilder = PublicClientApplicationBuilder.Create(clientId)
                        .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
                        .WithRedirectUri(redirectUrl)
                        .Build();
        var scope = serviceUrl + "/user_impersonation";
        string[] scopes = { scope };
        // First try to get an authentication token from the cache using a hint.
        AuthenticationResult authBuilderResult=null;
        try
        {
            authBuilderResult = authBuilder.AcquireTokenSilent(scopes, username)
               .ExecuteAsync().Result;
        }
        catch (Exception ex)
        {
            System.Diagnostics.Debug.WriteLine(
                $"Error acquiring auth token from cache:{System.Environment.NewLine}{ex}");
            // Token cache request failed, so request a new token.
            try
            {
                if (username != string.Empty && password != string.Empty)
                {
                    // Request a token based on username/password credentials.
                    authBuilderResult = authBuilder.AcquireTokenByUsernamePassword(scopes, username, password)
                                .ExecuteAsync().Result;
                }
                else
                {
                    // Prompt the user for credentials and get the token.
                    authBuilderResult = authBuilder.AcquireTokenInteractive(scopes)
                                .ExecuteAsync().Result;
                }
            }
            catch (Exception msalex)
            {
                System.Diagnostics.Debug.WriteLine(
                    $"Error acquiring auth token with user credentials:{System.Environment.NewLine}{msalex}");
                throw;
            }
        }
        //Note that an Microsoft Entra ID access token has finite lifetime, default expiration is 60 minutes.
        authHeader = new AuthenticationHeaderValue("Bearer", authBuilderResult.AccessToken);
    }

    protected override Task<HttpResponseMessage> SendAsync(
              HttpRequestMessage request, System.Threading.CancellationToken cancellationToken)
    {
        request.Headers.Authorization = authHeader;
        return base.SendAsync(request, cancellationToken);
    }
}
```

--- 

At this point, I am pretty sure I am in the right spot because I see familiar-looking instructions on **Connecting an app**:


### [Connect as an app](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth#connect-as-an-app)

Also contains: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth#connect-using-the-application-secret 

This looks like a familiar pattern to me, with an app ID, a secret ID, and a secret key. So I am pretty sure I am in the right place, but I will not that I am no longer on pages with info about Microsoft Dynamics -- this is all about Microsoft Dataverse. So maybe I am not in the right place. 
