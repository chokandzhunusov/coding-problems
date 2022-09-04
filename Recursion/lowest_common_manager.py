"""
Time complexity: O(n) number of nodes.
Space complexity: O(d) max depth of current iteraction branch.
"""


from typing import Optional


class OrgChart:
    def __init__(self, name, direct_reports=[]):
        self.name = name
        self.direct_reports = direct_reports


class OrgInfo:
    def __init__(self, lowest_common_manager: 'Optional[OrgChart]', num_of_important_reports: 'int'):
        self.lowest_common_manager = lowest_common_manager
        self.num_of_important_reports = num_of_important_reports


def get_org_info(manager: 'OrgChart', report_one: 'OrgChart', report_two: 'OrgChart'):
    num_of_important_reports = 0
    for report in manager.direct_reports:
        org_info = get_org_info(report, report_one, report_two)
        if org_info.lowest_common_manager:
            return org_info
        num_of_important_reports += org_info.num_of_important_reports

    if manager == report_one or manager == report_two:
        num_of_important_reports += 1

    lowest_common_manager = manager if num_of_important_reports == 2 else None
    return OrgInfo(lowest_common_manager, num_of_important_reports)


def get_lowest_common_manager(top_manager: 'OrgChart', report_one: 'OrgChart', report_two: 'OrgChart'):
    return get_org_info(top_manager, report_one, report_two).lowest_common_manager


def main() -> None:
    H = OrgChart(name='H')
    I = OrgChart(name='I')
    G = OrgChart(name='G')
    F = OrgChart(name='F')
    E = OrgChart(name='E')
    D = OrgChart(name='D', direct_reports=[I, H])
    C = OrgChart(name='C', direct_reports=[F, G])
    B = OrgChart(name='B', direct_reports=[D, E])
    A = OrgChart(name='A', direct_reports=[B, C])
    assert get_lowest_common_manager(A, E, I).name == 'B'


if __name__ == '__main__':
    main()
