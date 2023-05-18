// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appsync

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppSync::DataSource
func LookupDataSource(ctx *pulumi.Context, args *LookupDataSourceArgs, opts ...pulumi.InvokeOption) (*LookupDataSourceResult, error) {
	var rv LookupDataSourceResult
	err := ctx.Invoke("aws-native:appsync:getDataSource", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataSourceArgs struct {
	Id string `pulumi:"id"`
}

type LookupDataSourceResult struct {
	DataSourceArn            *string                             `pulumi:"dataSourceArn"`
	Description              *string                             `pulumi:"description"`
	DynamoDBConfig           *DataSourceDynamoDBConfig           `pulumi:"dynamoDBConfig"`
	ElasticsearchConfig      *DataSourceElasticsearchConfig      `pulumi:"elasticsearchConfig"`
	EventBridgeConfig        *DataSourceEventBridgeConfig        `pulumi:"eventBridgeConfig"`
	HttpConfig               *DataSourceHttpConfig               `pulumi:"httpConfig"`
	Id                       *string                             `pulumi:"id"`
	LambdaConfig             *DataSourceLambdaConfig             `pulumi:"lambdaConfig"`
	OpenSearchServiceConfig  *DataSourceOpenSearchServiceConfig  `pulumi:"openSearchServiceConfig"`
	RelationalDatabaseConfig *DataSourceRelationalDatabaseConfig `pulumi:"relationalDatabaseConfig"`
	ServiceRoleArn           *string                             `pulumi:"serviceRoleArn"`
	Type                     *string                             `pulumi:"type"`
}

func LookupDataSourceOutput(ctx *pulumi.Context, args LookupDataSourceOutputArgs, opts ...pulumi.InvokeOption) LookupDataSourceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataSourceResult, error) {
			args := v.(LookupDataSourceArgs)
			r, err := LookupDataSource(ctx, &args, opts...)
			var s LookupDataSourceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataSourceResultOutput)
}

type LookupDataSourceOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDataSourceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataSourceArgs)(nil)).Elem()
}

type LookupDataSourceResultOutput struct{ *pulumi.OutputState }

func (LookupDataSourceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataSourceResult)(nil)).Elem()
}

func (o LookupDataSourceResultOutput) ToLookupDataSourceResultOutput() LookupDataSourceResultOutput {
	return o
}

func (o LookupDataSourceResultOutput) ToLookupDataSourceResultOutputWithContext(ctx context.Context) LookupDataSourceResultOutput {
	return o
}

func (o LookupDataSourceResultOutput) DataSourceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.DataSourceArn }).(pulumi.StringPtrOutput)
}

func (o LookupDataSourceResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupDataSourceResultOutput) DynamoDBConfig() DataSourceDynamoDBConfigPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceDynamoDBConfig { return v.DynamoDBConfig }).(DataSourceDynamoDBConfigPtrOutput)
}

func (o LookupDataSourceResultOutput) ElasticsearchConfig() DataSourceElasticsearchConfigPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceElasticsearchConfig { return v.ElasticsearchConfig }).(DataSourceElasticsearchConfigPtrOutput)
}

func (o LookupDataSourceResultOutput) EventBridgeConfig() DataSourceEventBridgeConfigPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceEventBridgeConfig { return v.EventBridgeConfig }).(DataSourceEventBridgeConfigPtrOutput)
}

func (o LookupDataSourceResultOutput) HttpConfig() DataSourceHttpConfigPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceHttpConfig { return v.HttpConfig }).(DataSourceHttpConfigPtrOutput)
}

func (o LookupDataSourceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDataSourceResultOutput) LambdaConfig() DataSourceLambdaConfigPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceLambdaConfig { return v.LambdaConfig }).(DataSourceLambdaConfigPtrOutput)
}

func (o LookupDataSourceResultOutput) OpenSearchServiceConfig() DataSourceOpenSearchServiceConfigPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceOpenSearchServiceConfig { return v.OpenSearchServiceConfig }).(DataSourceOpenSearchServiceConfigPtrOutput)
}

func (o LookupDataSourceResultOutput) RelationalDatabaseConfig() DataSourceRelationalDatabaseConfigPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceRelationalDatabaseConfig { return v.RelationalDatabaseConfig }).(DataSourceRelationalDatabaseConfigPtrOutput)
}

func (o LookupDataSourceResultOutput) ServiceRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.ServiceRoleArn }).(pulumi.StringPtrOutput)
}

func (o LookupDataSourceResultOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.Type }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataSourceResultOutput{})
}
