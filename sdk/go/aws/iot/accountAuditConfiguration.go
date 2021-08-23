// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html
type AccountAuditConfiguration struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations
	AuditCheckConfigurations AccountAuditConfigurationAuditCheckConfigurationsOutput `pulumi:"auditCheckConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations
	AuditNotificationTargetConfigurations AccountAuditConfigurationAuditNotificationTargetConfigurationsPtrOutput `pulumi:"auditNotificationTargetConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
}

// NewAccountAuditConfiguration registers a new resource with the given unique name, arguments, and options.
func NewAccountAuditConfiguration(ctx *pulumi.Context,
	name string, args *AccountAuditConfigurationArgs, opts ...pulumi.ResourceOption) (*AccountAuditConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccountId == nil {
		return nil, errors.New("invalid value for required argument 'AccountId'")
	}
	if args.AuditCheckConfigurations == nil {
		return nil, errors.New("invalid value for required argument 'AuditCheckConfigurations'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource AccountAuditConfiguration
	err := ctx.RegisterResource("aws-native:iot:AccountAuditConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccountAuditConfiguration gets an existing AccountAuditConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccountAuditConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccountAuditConfigurationState, opts ...pulumi.ResourceOption) (*AccountAuditConfiguration, error) {
	var resource AccountAuditConfiguration
	err := ctx.ReadResource("aws-native:iot:AccountAuditConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccountAuditConfiguration resources.
type accountAuditConfigurationState struct {
}

type AccountAuditConfigurationState struct {
}

func (AccountAuditConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*accountAuditConfigurationState)(nil)).Elem()
}

type accountAuditConfigurationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid
	AccountId string `pulumi:"accountId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations
	AuditCheckConfigurations AccountAuditConfigurationAuditCheckConfigurations `pulumi:"auditCheckConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations
	AuditNotificationTargetConfigurations *AccountAuditConfigurationAuditNotificationTargetConfigurations `pulumi:"auditNotificationTargetConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn
	RoleArn string `pulumi:"roleArn"`
}

// The set of arguments for constructing a AccountAuditConfiguration resource.
type AccountAuditConfigurationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid
	AccountId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations
	AuditCheckConfigurations AccountAuditConfigurationAuditCheckConfigurationsInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations
	AuditNotificationTargetConfigurations AccountAuditConfigurationAuditNotificationTargetConfigurationsPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn
	RoleArn pulumi.StringInput
}

func (AccountAuditConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accountAuditConfigurationArgs)(nil)).Elem()
}

type AccountAuditConfigurationInput interface {
	pulumi.Input

	ToAccountAuditConfigurationOutput() AccountAuditConfigurationOutput
	ToAccountAuditConfigurationOutputWithContext(ctx context.Context) AccountAuditConfigurationOutput
}

func (*AccountAuditConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountAuditConfiguration)(nil))
}

func (i *AccountAuditConfiguration) ToAccountAuditConfigurationOutput() AccountAuditConfigurationOutput {
	return i.ToAccountAuditConfigurationOutputWithContext(context.Background())
}

func (i *AccountAuditConfiguration) ToAccountAuditConfigurationOutputWithContext(ctx context.Context) AccountAuditConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccountAuditConfigurationOutput)
}

type AccountAuditConfigurationOutput struct{ *pulumi.OutputState }

func (AccountAuditConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountAuditConfiguration)(nil))
}

func (o AccountAuditConfigurationOutput) ToAccountAuditConfigurationOutput() AccountAuditConfigurationOutput {
	return o
}

func (o AccountAuditConfigurationOutput) ToAccountAuditConfigurationOutputWithContext(ctx context.Context) AccountAuditConfigurationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AccountAuditConfigurationOutput{})
}
