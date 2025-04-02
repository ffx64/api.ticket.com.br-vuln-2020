███████████████████████████████████████████████████████████████████████████████  
█                                                                             █  
█                Brazilian CPF Data Extractor - api.ticket.com.br             █  
█                   (Automating Brazilian CPF data extraction)                █  
█                                                                             █  
███████████████████████████████████████████████████████████████████████████████  

In 2019, a critical vulnerability was found in the `ticket.com.br` API, allowing  
sensitive CPF data extraction. The day the flaw was discovered, it was reported to  
the responsible team. However, we have yet to receive any response or official  
recognition on the issue.  

After a few days of generating a significant number of requests to the API (to  
alert the severity of the issue), the team finally took action, taking the API  
down and fixing the vulnerability. It's important to note that, **at no point**,  
data was exposed publicly or accessed by third parties, as the tool was never in  
circulation outside a controlled environment.  

I am now exposing the **Proof of Concept (PoC)** that was ignored at the time.  

**Important: The script no longer works**  

The vulnerability has been fixed, and the script **no longer functions**. Below  
are the features the script had while the flaw was active:  

- Made requests to the public API of `ticket.com.br` (URL:  
`https://api.ticket.com.br/ticketshop/v1/simulacao/{random}/cliente`) to collect CPF data.  

- Extracted data such as:  
  - **CPF**  
  - **Company Name** (when applicable to a legal entity)  
  - **Date of Birth**  
  - **Phones** (Business and Mobile)  
  - **User Name**  
  - **Full Address** (Zip Code, Street, Number, Complement, Neighborhood,  
  State, City)  
  - **Last update date**  
- Checked if the CPF was from a legal entity and processed only data of  
individuals.  
- Saved extracted data in a **CSV** file.  

I would like to highlight that, while the script was used in a controlled manner,  
its main purpose was always to alert the team about the problem. After the fix,  
the tool became obsolete.  

Data exposure never happened improperly, and the purpose was always security  
and awareness.