// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// StackSet as a resource provides one-click experience for provisioning a StackSet and StackInstances
type StackSet struct {
	pulumi.CustomResourceState

	// The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
	AdministrationRoleArn pulumi.StringPtrOutput `pulumi:"administrationRoleArn"`
	// Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
	AutoDeployment StackSetAutoDeploymentPtrOutput `pulumi:"autoDeployment"`
	// Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
	CallAs StackSetCallAsPtrOutput `pulumi:"callAs"`
	// In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
	Capabilities StackSetCapabilityArrayOutput `pulumi:"capabilities"`
	// A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
	ExecutionRoleName pulumi.StringPtrOutput `pulumi:"executionRoleName"`
	// Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
	ManagedExecution     ManagedExecutionPropertiesPtrOutput   `pulumi:"managedExecution"`
	OperationPreferences StackSetOperationPreferencesPtrOutput `pulumi:"operationPreferences"`
	// The input parameters for the stack set template.
	Parameters StackSetParameterArrayOutput `pulumi:"parameters"`
	// Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
	PermissionModel StackSetPermissionModelOutput `pulumi:"permissionModel"`
	// A group of stack instances with parameters in some specific accounts and regions.
	StackInstancesGroup StackSetStackInstancesArrayOutput `pulumi:"stackInstancesGroup"`
	// The ID of the stack set that you're creating.
	StackSetId pulumi.StringOutput `pulumi:"stackSetId"`
	// The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
	StackSetName pulumi.StringOutput `pulumi:"stackSetName"`
	// The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
	Tags StackSetTagArrayOutput `pulumi:"tags"`
	// The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
	TemplateBody pulumi.StringPtrOutput `pulumi:"templateBody"`
	// Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
	TemplateUrl pulumi.StringPtrOutput `pulumi:"templateUrl"`
}

// NewStackSet registers a new resource with the given unique name, arguments, and options.
func NewStackSet(ctx *pulumi.Context,
	name string, args *StackSetArgs, opts ...pulumi.ResourceOption) (*StackSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PermissionModel == nil {
		return nil, errors.New("invalid value for required argument 'PermissionModel'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource StackSet
	err := ctx.RegisterResource("aws-native:cloudformation:StackSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStackSet gets an existing StackSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStackSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StackSetState, opts ...pulumi.ResourceOption) (*StackSet, error) {
	var resource StackSet
	err := ctx.ReadResource("aws-native:cloudformation:StackSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StackSet resources.
type stackSetState struct {
}

type StackSetState struct {
}

func (StackSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*stackSetState)(nil)).Elem()
}

type stackSetArgs struct {
	// The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
	AdministrationRoleArn *string `pulumi:"administrationRoleArn"`
	// Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
	AutoDeployment *StackSetAutoDeployment `pulumi:"autoDeployment"`
	// Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
	CallAs *StackSetCallAs `pulumi:"callAs"`
	// In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
	Capabilities []StackSetCapability `pulumi:"capabilities"`
	// A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
	Description *string `pulumi:"description"`
	// The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
	ExecutionRoleName *string `pulumi:"executionRoleName"`
	// Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
	ManagedExecution     *ManagedExecutionProperties   `pulumi:"managedExecution"`
	OperationPreferences *StackSetOperationPreferences `pulumi:"operationPreferences"`
	// The input parameters for the stack set template.
	Parameters []StackSetParameter `pulumi:"parameters"`
	// Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
	PermissionModel StackSetPermissionModel `pulumi:"permissionModel"`
	// A group of stack instances with parameters in some specific accounts and regions.
	StackInstancesGroup []StackSetStackInstances `pulumi:"stackInstancesGroup"`
	// The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
	StackSetName *string `pulumi:"stackSetName"`
	// The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
	Tags []StackSetTag `pulumi:"tags"`
	// The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
	TemplateBody *string `pulumi:"templateBody"`
	// Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
	TemplateUrl *string `pulumi:"templateUrl"`
}

// The set of arguments for constructing a StackSet resource.
type StackSetArgs struct {
	// The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
	AdministrationRoleArn pulumi.StringPtrInput
	// Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
	AutoDeployment StackSetAutoDeploymentPtrInput
	// Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
	CallAs StackSetCallAsPtrInput
	// In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
	Capabilities StackSetCapabilityArrayInput
	// A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
	Description pulumi.StringPtrInput
	// The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
	ExecutionRoleName pulumi.StringPtrInput
	// Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
	ManagedExecution     ManagedExecutionPropertiesPtrInput
	OperationPreferences StackSetOperationPreferencesPtrInput
	// The input parameters for the stack set template.
	Parameters StackSetParameterArrayInput
	// Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
	PermissionModel StackSetPermissionModelInput
	// A group of stack instances with parameters in some specific accounts and regions.
	StackInstancesGroup StackSetStackInstancesArrayInput
	// The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
	StackSetName pulumi.StringPtrInput
	// The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
	Tags StackSetTagArrayInput
	// The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
	TemplateBody pulumi.StringPtrInput
	// Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
	TemplateUrl pulumi.StringPtrInput
}

func (StackSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stackSetArgs)(nil)).Elem()
}

type StackSetInput interface {
	pulumi.Input

	ToStackSetOutput() StackSetOutput
	ToStackSetOutputWithContext(ctx context.Context) StackSetOutput
}

func (*StackSet) ElementType() reflect.Type {
	return reflect.TypeOf((**StackSet)(nil)).Elem()
}

func (i *StackSet) ToStackSetOutput() StackSetOutput {
	return i.ToStackSetOutputWithContext(context.Background())
}

func (i *StackSet) ToStackSetOutputWithContext(ctx context.Context) StackSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackSetOutput)
}

type StackSetOutput struct{ *pulumi.OutputState }

func (StackSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StackSet)(nil)).Elem()
}

func (o StackSetOutput) ToStackSetOutput() StackSetOutput {
	return o
}

func (o StackSetOutput) ToStackSetOutputWithContext(ctx context.Context) StackSetOutput {
	return o
}

// The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
func (o StackSetOutput) AdministrationRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StackSet) pulumi.StringPtrOutput { return v.AdministrationRoleArn }).(pulumi.StringPtrOutput)
}

// Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
func (o StackSetOutput) AutoDeployment() StackSetAutoDeploymentPtrOutput {
	return o.ApplyT(func(v *StackSet) StackSetAutoDeploymentPtrOutput { return v.AutoDeployment }).(StackSetAutoDeploymentPtrOutput)
}

// Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
func (o StackSetOutput) CallAs() StackSetCallAsPtrOutput {
	return o.ApplyT(func(v *StackSet) StackSetCallAsPtrOutput { return v.CallAs }).(StackSetCallAsPtrOutput)
}

// In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
func (o StackSetOutput) Capabilities() StackSetCapabilityArrayOutput {
	return o.ApplyT(func(v *StackSet) StackSetCapabilityArrayOutput { return v.Capabilities }).(StackSetCapabilityArrayOutput)
}

// A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
func (o StackSetOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StackSet) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
func (o StackSetOutput) ExecutionRoleName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StackSet) pulumi.StringPtrOutput { return v.ExecutionRoleName }).(pulumi.StringPtrOutput)
}

// Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
func (o StackSetOutput) ManagedExecution() ManagedExecutionPropertiesPtrOutput {
	return o.ApplyT(func(v *StackSet) ManagedExecutionPropertiesPtrOutput { return v.ManagedExecution }).(ManagedExecutionPropertiesPtrOutput)
}

func (o StackSetOutput) OperationPreferences() StackSetOperationPreferencesPtrOutput {
	return o.ApplyT(func(v *StackSet) StackSetOperationPreferencesPtrOutput { return v.OperationPreferences }).(StackSetOperationPreferencesPtrOutput)
}

// The input parameters for the stack set template.
func (o StackSetOutput) Parameters() StackSetParameterArrayOutput {
	return o.ApplyT(func(v *StackSet) StackSetParameterArrayOutput { return v.Parameters }).(StackSetParameterArrayOutput)
}

// Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
func (o StackSetOutput) PermissionModel() StackSetPermissionModelOutput {
	return o.ApplyT(func(v *StackSet) StackSetPermissionModelOutput { return v.PermissionModel }).(StackSetPermissionModelOutput)
}

// A group of stack instances with parameters in some specific accounts and regions.
func (o StackSetOutput) StackInstancesGroup() StackSetStackInstancesArrayOutput {
	return o.ApplyT(func(v *StackSet) StackSetStackInstancesArrayOutput { return v.StackInstancesGroup }).(StackSetStackInstancesArrayOutput)
}

// The ID of the stack set that you're creating.
func (o StackSetOutput) StackSetId() pulumi.StringOutput {
	return o.ApplyT(func(v *StackSet) pulumi.StringOutput { return v.StackSetId }).(pulumi.StringOutput)
}

// The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
func (o StackSetOutput) StackSetName() pulumi.StringOutput {
	return o.ApplyT(func(v *StackSet) pulumi.StringOutput { return v.StackSetName }).(pulumi.StringOutput)
}

// The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
func (o StackSetOutput) Tags() StackSetTagArrayOutput {
	return o.ApplyT(func(v *StackSet) StackSetTagArrayOutput { return v.Tags }).(StackSetTagArrayOutput)
}

// The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
func (o StackSetOutput) TemplateBody() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StackSet) pulumi.StringPtrOutput { return v.TemplateBody }).(pulumi.StringPtrOutput)
}

// Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
func (o StackSetOutput) TemplateUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StackSet) pulumi.StringPtrOutput { return v.TemplateUrl }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StackSetInput)(nil)).Elem(), &StackSet{})
	pulumi.RegisterOutputType(StackSetOutput{})
}
