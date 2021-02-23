# How to make an output report (case of future design)

# prior
1. connect to the platform via their account
2. activate the develop mode in the Odoo parameter setting (see this image)
- click on settings -> below the page: activate developer mode
        ![module setting](images/activation_modedevelopper.png)

# header and footer

## 1. configuration layout
- In the same window at "Business Documents" level, where it is written Layout
- click on Configure your document layout

    ![configuration layout](images/configurationlayout.png)

- among the basic model choose the model that suits you.
- add your company logo or header.
- choose the color.
- the police.
- the name of the company.
- footer information.
- the paper size.

- NB: this information is not binding but is necessary for a normal report.

- Then click on save.

## 2. Edit Layout
> In the same window at "Business Documents" level

- where it is written Layout
- click on Edit layout

   
you will be redirected to the QWEB page of the external_layout_standard view (view which supports the header and the footer)

- to modify the qweb code of the view just click on the EDIT button in hat on the left

- you must have knowledge of the qweb, the html or its use with bootstrap to make modifications because a false maneuver will cause an error and the modifications will not be saved

    ![edit layout](images/editexternal.png)

- NB: your layout must be selected by default (you will see it clearly when you are in develop mode)

    ![default layout](images/default.png)

# Edit sales report / quotation order / delivery

## 1. Two ways to proceed either by searching directly for the name of the view or the report
- click on the setting option
- in the navbar or menu bar at the top click on Technical
- on the submenu that appears click either on view or report

    ![rapport](images/rapport.png)

    ![vue](images/vue.png)

   - example at the report level, in the search bar on the right type "quotation" then validate

        ![quotation](images/quotation.png)
            
        - by selecting the first line "Quotation / Order"
        
        ![report quotation order](images/report_quotation_order.png)

        - to have the possibility to modify the report, click on the qweb tab to the right of the "Qweb views" modal.
            you access the different views of the report that you can then modify

        ![report vue modifier](images/rapport_vue_qweb.png)

        
        - for the "report_saleorder_document" view of the "Quotation" report, you therefore have the possibility here to edit

            ![edit quoation](images/edit_quoation.png)

        
    - example at the view level (if you know its name directly) type "report_saleorder_document"

        ![report_saleorder_document](images/report_saleorder_document.png)

        - select the view to modify (example for report_saleorder_document)

        ![report_saleorder_document_qweb](images/report_saleorder_document_qweb.png)

            
            - it only remains to edit

# print the report

## 1. Let us take the case of the sale because it is linked with the modfier report above (quaotation / report_saleorder_document)
- the sales module must exist beforehand
- click on the sales module
- click on create at the top right
- Fill in the sales information

    ![ventes](images/ventes.png)

- save
- In the middle above click on print> quotation / order

    ![print](images/print.png)

    ![rapport_pdf](images/rapport_pdf.png)








                
            






