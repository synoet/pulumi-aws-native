// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkfirewall

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource type definition for AWS::NetworkFirewall::LoggingConfiguration
func LookupLoggingConfiguration(ctx *pulumi.Context, args *LookupLoggingConfigurationArgs, opts ...pulumi.InvokeOption) (*LookupLoggingConfigurationResult, error) {
	var rv LookupLoggingConfigurationResult
	err := ctx.Invoke("aws-native:networkfirewall:getLoggingConfiguration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLoggingConfigurationArgs struct {
	FirewallArn string `pulumi:"firewallArn"`
}

type LookupLoggingConfigurationResult struct {
	LoggingConfiguration *LoggingConfigurationType `pulumi:"loggingConfiguration"`
}

func LookupLoggingConfigurationOutput(ctx *pulumi.Context, args LookupLoggingConfigurationOutputArgs, opts ...pulumi.InvokeOption) LookupLoggingConfigurationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLoggingConfigurationResult, error) {
			args := v.(LookupLoggingConfigurationArgs)
			r, err := LookupLoggingConfiguration(ctx, &args, opts...)
			var s LookupLoggingConfigurationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLoggingConfigurationResultOutput)
}

type LookupLoggingConfigurationOutputArgs struct {
	FirewallArn pulumi.StringInput `pulumi:"firewallArn"`
}

func (LookupLoggingConfigurationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLoggingConfigurationArgs)(nil)).Elem()
}

type LookupLoggingConfigurationResultOutput struct{ *pulumi.OutputState }

func (LookupLoggingConfigurationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLoggingConfigurationResult)(nil)).Elem()
}

func (o LookupLoggingConfigurationResultOutput) ToLookupLoggingConfigurationResultOutput() LookupLoggingConfigurationResultOutput {
	return o
}

func (o LookupLoggingConfigurationResultOutput) ToLookupLoggingConfigurationResultOutputWithContext(ctx context.Context) LookupLoggingConfigurationResultOutput {
	return o
}

func (o LookupLoggingConfigurationResultOutput) LoggingConfiguration() LoggingConfigurationTypePtrOutput {
	return o.ApplyT(func(v LookupLoggingConfigurationResult) *LoggingConfigurationType { return v.LoggingConfiguration }).(LoggingConfigurationTypePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLoggingConfigurationResultOutput{})
}
