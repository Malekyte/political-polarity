import pandas as pd

congressPresidentParty = [
    (80, "Republican"),  # 1947-1949, President Truman (Democrat), but Republican-controlled Congress
    (81, "Democrat"),    # 1949-1951, President Truman (Democrat)
    (82, "Democrat"),    # 1951-1953, President Truman (Democrat)
    (83, "Republican"),  # 1953-1955, President Eisenhower (Republican)
    (84, "Republican"),  # 1955-1957, President Eisenhower (Republican)
    (85, "Republican"),  # 1957-1959, President Eisenhower (Republican)
    (86, "Republican"),  # 1959-1961, President Eisenhower (Republican)
    (87, "Democrat"),    # 1961-1963, President Kennedy (Democrat)
    (88, "Democrat"),    # 1963-1965, President Johnson (Democrat)
    (89, "Democrat"),    # 1965-1967, President Johnson (Democrat)
    (90, "Democrat"),    # 1967-1969, President Johnson (Democrat)
    (91, "Republican"),  # 1969-1971, President Nixon (Republican)
    (92, "Republican"),  # 1971-1973, President Nixon (Republican)
    (93, "Republican"),  # 1973-1975, President Nixon (Republican) / Ford (Republican)
    (94, "Republican"),  # 1975-1977, President Ford (Republican)
    (95, "Democrat"),    # 1977-1979, President Carter (Democrat)
    (96, "Democrat"),    # 1979-1981, President Carter (Democrat)
    (97, "Republican"),  # 1981-1983, President Reagan (Republican)
    (98, "Republican"),  # 1983-1985, President Reagan (Republican)
    (99, "Republican"),  # 1985-1987, President Reagan (Republican)
    (100, "Republican"), # 1987-1989, President Reagan (Republican)
    (101, "Republican"), # 1989-1991, President Bush (Republican)
    (102, "Republican"), # 1991-1993, President Bush (Republican)
    (103, "Democrat"),   # 1993-1995, President Clinton (Democrat)
    (104, "Democrat"),   # 1995-1997, President Clinton (Democrat)
    (105, "Democrat"),   # 1997-1999, President Clinton (Democrat)
    (106, "Democrat"),   # 1999-2001, President Clinton (Democrat)
    (107, "Republican"), # 2001-2003, President Bush (Republican)
    (108, "Republican"), # 2003-2005, President Bush (Republican)
    (109, "Republican"), # 2005-2007, President Bush (Republican)
    (110, "Republican"), # 2007-2009, President Bush (Republican)
    (111, "Democrat"),   # 2009-2011, President Obama (Democrat)
    (112, "Democrat"),   # 2011-2013, President Obama (Democrat)
    (113, "Democrat"),   # 2013-2015, President Obama (Democrat)
    (114, "Democrat"),   # 2015-2017, President Obama (Democrat)
    (115, "Republican"), # 2017-2019, President Trump (Republican)
    (116, "Republican"), # 2019-2021, President Trump (Republican)
    (117, "Democrat"),   # 2021-2023, President Biden (Democrat)
    (118, "Democrat")    # 2023-2025, President Biden (Democrat)
]

event_timeline = pd.DataFrame(
    columns= ['start', 'stop', 'event', 'type'],
    data= [
        [1861, 1865, 'American Civil War', 'War'],
        [1863, pd.NA, 'Emancipation Proclamation', 'War'],
        [1865, pd.NA, 'Lincoln Assassination', 'Terrorism'],
        [1873, pd.NA, 'Colfax Massacre', 'Terrorism'],
        [1881, pd.NA, 'Garfield Assassination', 'Terrorism'],
        [1898, pd.NA, 'Spanish-American War', 'War'],
        [1901, pd.NA, 'McKinley Assassination', 'Terrorism'],
        [1914, 1918, 'World War I', 'War'],
        [1920, pd.NA, '19th Amendment', 'Societal'],
        [1929, pd.NA, 'Great Depression', 'Economic'],
        [1934, pd.NA, 'Great Plains Dust Bowl', 'Economic'],
        [1939, 1945, 'World War II', 'War'],
        [1945, 1991, 'Cold War', 'War'],
        [1950, 1953, 'Korean War', 'War'],
        [1955, 1975, 'Vietnam War', 'War'],
        [1963, pd.NA, 'Kennedy Assassination', 'Terrorism'],
        [1968, pd.NA, 'MLK Jr Assassination', 'Societal'],
        [1974, pd.NA, 'Watergate Scandal', 'Societal'],
        [2001, pd.NA, '9/11 Attacks', 'Terrorism'],
        [2003, 2011, 'Iraq War', 'War'],
        [2013, pd.NA, 'Black Lives Matter', 'Societal']
    ]
)