from flask import Flask, request, Response, abort
import json
import tv, soundbar

app = Flask(__name__)

ACTION_PARAM = "action"


@app.route('/tv', methods = ['POST'])
def tvCommand():
  tv.handleAction(__getActionParam(request))
  return __getSuccessResponse()

@app.route('/soundbar', methods = ['POST'])
def soundbarCommand():
  soundbar.handleAction(__getActionParam(request))
  return __getSuccessResponse()

def __getActionParam(request):
  action = request.args.get(ACTION_PARAM, "")
  if not action:
    print(request.args)
    abort(400)
  return action

def __getSuccessResponse():
  return Response({"status": "ok"}, status=200, mimetype='application/json')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')