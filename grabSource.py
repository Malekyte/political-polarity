import requests
import sys
from pathlib import Path

def download_file(
    url:str,
    fpath:str = "",
    fname:str = None,
    path_type:bool = True,
    overwrite:bool = True
):
    '''
    Download a file from <url> to the <fpath>/<fname> location.

    Arguments:
              url: (str) Full source url location for download file. String must
                   include full http header.
            fpath: (str) Folder path to output file location. None default sets
                   output to current working directory. Use raw string literals
                   to prevent escape character evaluations.
            fname: (str) Output file name, including extension code. None default
                   will utilize final path element of url string.
        path_type: (bool) Type of fpath variable string. Default is True.
                     True = relative from current working directory;
                     False = Absolute file path.
        overwrite: (bool) Output file will overwrite existing file, if it
                   exists. Default option is True.

    Returns:
        None
    '''
    # determine pathing
    if path_type:
        _path = Path.cwd() / fpath
    elif not fpath:
        # raise error on calling for absolute path but no path was given
        pass
    else:
        _path = Path(fpath)
  
    # create folder if it doesn't exist
    _path.mkdir(parents= True, exist_ok= True)

    # append filename for output
    if fname:
        _path = _path / fname
    else:
        _path = _path / url.split("/")[-1]
  
    try:
        response = requests.get(url)
        response.raise_for_status()
        if overwrite:
            with open(_path, 'wb') as f:
                f.write(response.content)
        else:
            with open(_path, 'xb') as f:
                f.write(response.content)
        print(f"File saved successfully at: {_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file: {e}")
    except FileExistsError:
        print(f"Failed to write file, {fname} already exists and overwrite is disabled.")

if __name__ == "__main__":
    args = sys.argv
    o = False
    if len(args) > 1:
        a1 = args[1]
        if a1 == 'overwrite':
            o = True
    _p = Path().cwd() / "data" / "MemberIdeology.csv"
    if _p.exists() and not o:
        print(f"{_p.name} already exists.")
    else:
        print(f"Downloading {_p.name}.")
        download_file(
            "https://voteview.com/static/data/out/members/HSall_members.csv",
            fpath= "data",
            fname= "MemberIdeology.csv",
            overwrite= o
        )
        print(f"Download of {_p.name} complete.")
    _p = Path().cwd() / "data" / "MemberVotes.csv"
    if _p.exists() and not o:
        print(f"{_p.name} already exists.")
    else:
        print(f"Downloading {_p.name}.")
        download_file(
            "https://voteview.com/static/data/out/votes/HSall_votes.csv",
            fpath= "data",
            fname= "MemberVotes.csv",
            overwrite= o
        )
        print(f"Download of {_p.name} complete.")
    _p = Path().cwd() / "data" / "CongressionalVotes.csv"
    if _p.exists() and not o:
        print(f"{_p.name} already exists.")
    else:
        print(f"Downloading {_p.name}.")
        download_file(
            "https://voteview.com/static/data/out/rollcalls/HSall_rollcalls.csv",
            fpath= "data",
            fname= "CongressionalVotes.csv",
            overwrite= o
        )
        print(f"Download of {_p.name} complete.")