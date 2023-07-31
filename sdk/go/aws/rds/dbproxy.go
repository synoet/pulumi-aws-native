// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::RDS::DBProxy
type DBProxy struct {
	pulumi.CustomResourceState

	// The authorization mechanism that the proxy uses.
	Auth DBProxyAuthFormatArrayOutput `pulumi:"auth"`
	// The Amazon Resource Name (ARN) for the proxy.
	DbProxyArn pulumi.StringOutput `pulumi:"dbProxyArn"`
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName pulumi.StringOutput `pulumi:"dbProxyName"`
	// Whether the proxy includes detailed information about SQL statements in its logs.
	DebugLogging pulumi.BoolPtrOutput `pulumi:"debugLogging"`
	// The endpoint that you can use to connect to the proxy. You include the endpoint value in the connection string for a database client application.
	Endpoint pulumi.StringOutput `pulumi:"endpoint"`
	// The kinds of databases that the proxy can connect to.
	EngineFamily DBProxyEngineFamilyOutput `pulumi:"engineFamily"`
	// The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.
	IdleClientTimeout pulumi.IntPtrOutput `pulumi:"idleClientTimeout"`
	// A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.
	RequireTls pulumi.BoolPtrOutput `pulumi:"requireTls"`
	// The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
	Tags DBProxyTagFormatArrayOutput `pulumi:"tags"`
	// VPC ID to associate with the new DB proxy.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
	// VPC security group IDs to associate with the new proxy.
	VpcSecurityGroupIds pulumi.StringArrayOutput `pulumi:"vpcSecurityGroupIds"`
	// VPC subnet IDs to associate with the new proxy.
	VpcSubnetIds pulumi.StringArrayOutput `pulumi:"vpcSubnetIds"`
}

// NewDBProxy registers a new resource with the given unique name, arguments, and options.
func NewDBProxy(ctx *pulumi.Context,
	name string, args *DBProxyArgs, opts ...pulumi.ResourceOption) (*DBProxy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Auth == nil {
		return nil, errors.New("invalid value for required argument 'Auth'")
	}
	if args.EngineFamily == nil {
		return nil, errors.New("invalid value for required argument 'EngineFamily'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	if args.VpcSubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'VpcSubnetIds'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DBProxy
	err := ctx.RegisterResource("aws-native:rds:DBProxy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDBProxy gets an existing DBProxy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDBProxy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DBProxyState, opts ...pulumi.ResourceOption) (*DBProxy, error) {
	var resource DBProxy
	err := ctx.ReadResource("aws-native:rds:DBProxy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DBProxy resources.
type dbproxyState struct {
}

type DBProxyState struct {
}

func (DBProxyState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbproxyState)(nil)).Elem()
}

type dbproxyArgs struct {
	// The authorization mechanism that the proxy uses.
	Auth []DBProxyAuthFormat `pulumi:"auth"`
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName *string `pulumi:"dbProxyName"`
	// Whether the proxy includes detailed information about SQL statements in its logs.
	DebugLogging *bool `pulumi:"debugLogging"`
	// The kinds of databases that the proxy can connect to.
	EngineFamily DBProxyEngineFamily `pulumi:"engineFamily"`
	// The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.
	IdleClientTimeout *int `pulumi:"idleClientTimeout"`
	// A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.
	RequireTls *bool `pulumi:"requireTls"`
	// The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.
	RoleArn string `pulumi:"roleArn"`
	// An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
	Tags []DBProxyTagFormat `pulumi:"tags"`
	// VPC security group IDs to associate with the new proxy.
	VpcSecurityGroupIds []string `pulumi:"vpcSecurityGroupIds"`
	// VPC subnet IDs to associate with the new proxy.
	VpcSubnetIds []string `pulumi:"vpcSubnetIds"`
}

// The set of arguments for constructing a DBProxy resource.
type DBProxyArgs struct {
	// The authorization mechanism that the proxy uses.
	Auth DBProxyAuthFormatArrayInput
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName pulumi.StringPtrInput
	// Whether the proxy includes detailed information about SQL statements in its logs.
	DebugLogging pulumi.BoolPtrInput
	// The kinds of databases that the proxy can connect to.
	EngineFamily DBProxyEngineFamilyInput
	// The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.
	IdleClientTimeout pulumi.IntPtrInput
	// A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.
	RequireTls pulumi.BoolPtrInput
	// The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.
	RoleArn pulumi.StringInput
	// An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
	Tags DBProxyTagFormatArrayInput
	// VPC security group IDs to associate with the new proxy.
	VpcSecurityGroupIds pulumi.StringArrayInput
	// VPC subnet IDs to associate with the new proxy.
	VpcSubnetIds pulumi.StringArrayInput
}

func (DBProxyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbproxyArgs)(nil)).Elem()
}

type DBProxyInput interface {
	pulumi.Input

	ToDBProxyOutput() DBProxyOutput
	ToDBProxyOutputWithContext(ctx context.Context) DBProxyOutput
}

func (*DBProxy) ElementType() reflect.Type {
	return reflect.TypeOf((**DBProxy)(nil)).Elem()
}

func (i *DBProxy) ToDBProxyOutput() DBProxyOutput {
	return i.ToDBProxyOutputWithContext(context.Background())
}

func (i *DBProxy) ToDBProxyOutputWithContext(ctx context.Context) DBProxyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DBProxyOutput)
}

type DBProxyOutput struct{ *pulumi.OutputState }

func (DBProxyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DBProxy)(nil)).Elem()
}

func (o DBProxyOutput) ToDBProxyOutput() DBProxyOutput {
	return o
}

func (o DBProxyOutput) ToDBProxyOutputWithContext(ctx context.Context) DBProxyOutput {
	return o
}

// The authorization mechanism that the proxy uses.
func (o DBProxyOutput) Auth() DBProxyAuthFormatArrayOutput {
	return o.ApplyT(func(v *DBProxy) DBProxyAuthFormatArrayOutput { return v.Auth }).(DBProxyAuthFormatArrayOutput)
}

// The Amazon Resource Name (ARN) for the proxy.
func (o DBProxyOutput) DbProxyArn() pulumi.StringOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.StringOutput { return v.DbProxyArn }).(pulumi.StringOutput)
}

// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
func (o DBProxyOutput) DbProxyName() pulumi.StringOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.StringOutput { return v.DbProxyName }).(pulumi.StringOutput)
}

// Whether the proxy includes detailed information about SQL statements in its logs.
func (o DBProxyOutput) DebugLogging() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.BoolPtrOutput { return v.DebugLogging }).(pulumi.BoolPtrOutput)
}

// The endpoint that you can use to connect to the proxy. You include the endpoint value in the connection string for a database client application.
func (o DBProxyOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.StringOutput { return v.Endpoint }).(pulumi.StringOutput)
}

// The kinds of databases that the proxy can connect to.
func (o DBProxyOutput) EngineFamily() DBProxyEngineFamilyOutput {
	return o.ApplyT(func(v *DBProxy) DBProxyEngineFamilyOutput { return v.EngineFamily }).(DBProxyEngineFamilyOutput)
}

// The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.
func (o DBProxyOutput) IdleClientTimeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.IntPtrOutput { return v.IdleClientTimeout }).(pulumi.IntPtrOutput)
}

// A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.
func (o DBProxyOutput) RequireTls() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.BoolPtrOutput { return v.RequireTls }).(pulumi.BoolPtrOutput)
}

// The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.
func (o DBProxyOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

// An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
func (o DBProxyOutput) Tags() DBProxyTagFormatArrayOutput {
	return o.ApplyT(func(v *DBProxy) DBProxyTagFormatArrayOutput { return v.Tags }).(DBProxyTagFormatArrayOutput)
}

// VPC ID to associate with the new DB proxy.
func (o DBProxyOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.StringOutput { return v.VpcId }).(pulumi.StringOutput)
}

// VPC security group IDs to associate with the new proxy.
func (o DBProxyOutput) VpcSecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.StringArrayOutput { return v.VpcSecurityGroupIds }).(pulumi.StringArrayOutput)
}

// VPC subnet IDs to associate with the new proxy.
func (o DBProxyOutput) VpcSubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DBProxy) pulumi.StringArrayOutput { return v.VpcSubnetIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DBProxyInput)(nil)).Elem(), &DBProxy{})
	pulumi.RegisterOutputType(DBProxyOutput{})
}
