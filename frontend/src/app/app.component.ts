import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {

  tmp_server_url = process.env.NG_APP_GITPOD_WORKSPACE_URL;
  port = 5000
  server_url = `${this.tmp_server_url.substring(0,8)}${this.port}-${this.tmp_server_url.substring(8)}`;

  obsData: Observable<object>;

  constructor(private http: HttpClient) {}

  data: any = {};

  ngOnInit(): void {
    this.obsData = this.http.get(`${this.server_url}/api/user/1`);
    this.obsData.subscribe((data) => (this.data = data));
  }
}
