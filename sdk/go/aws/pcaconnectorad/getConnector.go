// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package pcaconnectorad

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::PCAConnectorAD::Connector Resource Type
func LookupConnector(ctx *pulumi.Context, args *LookupConnectorArgs, opts ...pulumi.InvokeOption) (*LookupConnectorResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupConnectorResult
	err := ctx.Invoke("aws-native:pcaconnectorad:getConnector", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupConnectorArgs struct {
	ConnectorArn string `pulumi:"connectorArn"`
}

type LookupConnectorResult struct {
	ConnectorArn *string `pulumi:"connectorArn"`
}

func LookupConnectorOutput(ctx *pulumi.Context, args LookupConnectorOutputArgs, opts ...pulumi.InvokeOption) LookupConnectorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupConnectorResult, error) {
			args := v.(LookupConnectorArgs)
			r, err := LookupConnector(ctx, &args, opts...)
			var s LookupConnectorResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupConnectorResultOutput)
}

type LookupConnectorOutputArgs struct {
	ConnectorArn pulumi.StringInput `pulumi:"connectorArn"`
}

func (LookupConnectorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConnectorArgs)(nil)).Elem()
}

type LookupConnectorResultOutput struct{ *pulumi.OutputState }

func (LookupConnectorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConnectorResult)(nil)).Elem()
}

func (o LookupConnectorResultOutput) ToLookupConnectorResultOutput() LookupConnectorResultOutput {
	return o
}

func (o LookupConnectorResultOutput) ToLookupConnectorResultOutputWithContext(ctx context.Context) LookupConnectorResultOutput {
	return o
}

func (o LookupConnectorResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupConnectorResult] {
	return pulumix.Output[LookupConnectorResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupConnectorResultOutput) ConnectorArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupConnectorResult) *string { return v.ConnectorArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupConnectorResultOutput{})
}
