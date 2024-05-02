from .dicts_datasus.ciha_dicts import ciha_dict
from .dicts_datasus.cnes_dicts import dc_dict, ee_dict, ef_dict, ep_dict, eq_dict, gm_dict, hb_dict, in_dict, lt_dict, pf_dict, rc_dict, sr_dict
from .dicts_datasus.pce_dicts import pce_dict
from .dicts_datasus.po_dicts import po_dict
from .dicts_datasus.resp_dicts import resp_dict
from .dicts_datasus.siasus_dicts import ab_dict,  acf_dict, ad_dict, am_dict, an_dict, aq_dict, ar_dict, atd_dict, pa_dict, ps_dict, sad_dict
from .dicts_datasus.sihsus_dicts import sp_dict, rd_dict


dict_datasus = {
    ('CIHA', 'CIHA'): ciha_dict,
    ('CNES', 'DC'): dc_dict,
    ('CNES', 'EE'): ee_dict,
    ('CNES', 'EF'): ef_dict,
    ('CNES', 'EP'): ep_dict,
    ('CNES', 'EQ'): eq_dict,
    ('CNES', 'GM'): gm_dict,
    ('CNES', 'HB'): hb_dict,
    ('CNES', 'IN'): in_dict,
    ('CNES', 'LT'): lt_dict,
    ('CNES', 'PF'): pf_dict,
    ('CNES', 'RC'): rc_dict,
    ('CNES', 'SR'): sr_dict,
    ('PCE', 'PCE'): pce_dict,
    ('PO', 'PO'): po_dict,
    ('RESP', 'RESP'): resp_dict,
    ('SIASUS', 'AB'): ab_dict,
    ('SIASUS', 'ACF'): acf_dict,
    ('SIASUS', 'AD'): ad_dict,
    ('SIASUS', 'AM'): am_dict,
    ('SIASUS', 'AN'): an_dict,
    ('SIASUS', 'AQ'): aq_dict,
    ('SIASUS', 'AR'): ar_dict,
    ('SIASUS', 'ATD'): atd_dict,
    ('SIASUS', 'PA'): pa_dict,
    ('SIASUS', 'PS'): ps_dict,
    ('SIASUS', 'SAD'): sad_dict,
    ('SIHSUS', 'SP'): sp_dict,
    ('SIHSUS', 'RD'): rd_dict

}