// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package chatbot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Chatbot::MicrosoftTeamsChannelConfiguration.
func LookupMicrosoftTeamsChannelConfiguration(ctx *pulumi.Context, args *LookupMicrosoftTeamsChannelConfigurationArgs, opts ...pulumi.InvokeOption) (*LookupMicrosoftTeamsChannelConfigurationResult, error) {
	var rv LookupMicrosoftTeamsChannelConfigurationResult
	err := ctx.Invoke("aws-native:chatbot:getMicrosoftTeamsChannelConfiguration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMicrosoftTeamsChannelConfigurationArgs struct {
	// Amazon Resource Name (ARN) of the configuration
	Arn string `pulumi:"arn"`
}

type LookupMicrosoftTeamsChannelConfigurationResult struct {
	// Amazon Resource Name (ARN) of the configuration
	Arn *string `pulumi:"arn"`
	// The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
	GuardrailPolicies []string `pulumi:"guardrailPolicies"`
	// The ARN of the IAM role that defines the permissions for AWS Chatbot
	IamRoleArn *string `pulumi:"iamRoleArn"`
	// Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs
	LoggingLevel *string `pulumi:"loggingLevel"`
	// ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.
	SnsTopicArns []string `pulumi:"snsTopicArns"`
	// The id of the Microsoft Teams channel
	TeamsChannelId *string `pulumi:"teamsChannelId"`
	// Enables use of a user role requirement in your chat configuration
	UserRoleRequired *bool `pulumi:"userRoleRequired"`
}

func LookupMicrosoftTeamsChannelConfigurationOutput(ctx *pulumi.Context, args LookupMicrosoftTeamsChannelConfigurationOutputArgs, opts ...pulumi.InvokeOption) LookupMicrosoftTeamsChannelConfigurationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMicrosoftTeamsChannelConfigurationResult, error) {
			args := v.(LookupMicrosoftTeamsChannelConfigurationArgs)
			r, err := LookupMicrosoftTeamsChannelConfiguration(ctx, &args, opts...)
			var s LookupMicrosoftTeamsChannelConfigurationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMicrosoftTeamsChannelConfigurationResultOutput)
}

type LookupMicrosoftTeamsChannelConfigurationOutputArgs struct {
	// Amazon Resource Name (ARN) of the configuration
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupMicrosoftTeamsChannelConfigurationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMicrosoftTeamsChannelConfigurationArgs)(nil)).Elem()
}

type LookupMicrosoftTeamsChannelConfigurationResultOutput struct{ *pulumi.OutputState }

func (LookupMicrosoftTeamsChannelConfigurationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMicrosoftTeamsChannelConfigurationResult)(nil)).Elem()
}

func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) ToLookupMicrosoftTeamsChannelConfigurationResultOutput() LookupMicrosoftTeamsChannelConfigurationResultOutput {
	return o
}

func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) ToLookupMicrosoftTeamsChannelConfigurationResultOutputWithContext(ctx context.Context) LookupMicrosoftTeamsChannelConfigurationResultOutput {
	return o
}

// Amazon Resource Name (ARN) of the configuration
func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMicrosoftTeamsChannelConfigurationResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) GuardrailPolicies() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupMicrosoftTeamsChannelConfigurationResult) []string { return v.GuardrailPolicies }).(pulumi.StringArrayOutput)
}

// The ARN of the IAM role that defines the permissions for AWS Chatbot
func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) IamRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMicrosoftTeamsChannelConfigurationResult) *string { return v.IamRoleArn }).(pulumi.StringPtrOutput)
}

// Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs
func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) LoggingLevel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMicrosoftTeamsChannelConfigurationResult) *string { return v.LoggingLevel }).(pulumi.StringPtrOutput)
}

// ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.
func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) SnsTopicArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupMicrosoftTeamsChannelConfigurationResult) []string { return v.SnsTopicArns }).(pulumi.StringArrayOutput)
}

// The id of the Microsoft Teams channel
func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) TeamsChannelId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMicrosoftTeamsChannelConfigurationResult) *string { return v.TeamsChannelId }).(pulumi.StringPtrOutput)
}

// Enables use of a user role requirement in your chat configuration
func (o LookupMicrosoftTeamsChannelConfigurationResultOutput) UserRoleRequired() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupMicrosoftTeamsChannelConfigurationResult) *bool { return v.UserRoleRequired }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMicrosoftTeamsChannelConfigurationResultOutput{})
}
