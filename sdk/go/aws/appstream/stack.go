// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appstream

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppStream::Stack
//
// Deprecated: Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Stack struct {
	pulumi.CustomResourceState

	AccessEndpoints             StackAccessEndpointArrayOutput            `pulumi:"accessEndpoints"`
	ApplicationSettings         StackApplicationSettingsPtrOutput         `pulumi:"applicationSettings"`
	AttributesToDelete          pulumi.StringArrayOutput                  `pulumi:"attributesToDelete"`
	DeleteStorageConnectors     pulumi.BoolPtrOutput                      `pulumi:"deleteStorageConnectors"`
	Description                 pulumi.StringPtrOutput                    `pulumi:"description"`
	DisplayName                 pulumi.StringPtrOutput                    `pulumi:"displayName"`
	EmbedHostDomains            pulumi.StringArrayOutput                  `pulumi:"embedHostDomains"`
	FeedbackUrl                 pulumi.StringPtrOutput                    `pulumi:"feedbackUrl"`
	Name                        pulumi.StringPtrOutput                    `pulumi:"name"`
	RedirectUrl                 pulumi.StringPtrOutput                    `pulumi:"redirectUrl"`
	StorageConnectors           StackStorageConnectorArrayOutput          `pulumi:"storageConnectors"`
	StreamingExperienceSettings StackStreamingExperienceSettingsPtrOutput `pulumi:"streamingExperienceSettings"`
	Tags                        StackTagArrayOutput                       `pulumi:"tags"`
	UserSettings                StackUserSettingArrayOutput               `pulumi:"userSettings"`
}

// NewStack registers a new resource with the given unique name, arguments, and options.
func NewStack(ctx *pulumi.Context,
	name string, args *StackArgs, opts ...pulumi.ResourceOption) (*Stack, error) {
	if args == nil {
		args = &StackArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Stack
	err := ctx.RegisterResource("aws-native:appstream:Stack", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStack gets an existing Stack resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStack(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StackState, opts ...pulumi.ResourceOption) (*Stack, error) {
	var resource Stack
	err := ctx.ReadResource("aws-native:appstream:Stack", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Stack resources.
type stackState struct {
}

type StackState struct {
}

func (StackState) ElementType() reflect.Type {
	return reflect.TypeOf((*stackState)(nil)).Elem()
}

type stackArgs struct {
	AccessEndpoints             []StackAccessEndpoint             `pulumi:"accessEndpoints"`
	ApplicationSettings         *StackApplicationSettings         `pulumi:"applicationSettings"`
	AttributesToDelete          []string                          `pulumi:"attributesToDelete"`
	DeleteStorageConnectors     *bool                             `pulumi:"deleteStorageConnectors"`
	Description                 *string                           `pulumi:"description"`
	DisplayName                 *string                           `pulumi:"displayName"`
	EmbedHostDomains            []string                          `pulumi:"embedHostDomains"`
	FeedbackUrl                 *string                           `pulumi:"feedbackUrl"`
	Name                        *string                           `pulumi:"name"`
	RedirectUrl                 *string                           `pulumi:"redirectUrl"`
	StorageConnectors           []StackStorageConnector           `pulumi:"storageConnectors"`
	StreamingExperienceSettings *StackStreamingExperienceSettings `pulumi:"streamingExperienceSettings"`
	Tags                        []StackTag                        `pulumi:"tags"`
	UserSettings                []StackUserSetting                `pulumi:"userSettings"`
}

// The set of arguments for constructing a Stack resource.
type StackArgs struct {
	AccessEndpoints             StackAccessEndpointArrayInput
	ApplicationSettings         StackApplicationSettingsPtrInput
	AttributesToDelete          pulumi.StringArrayInput
	DeleteStorageConnectors     pulumi.BoolPtrInput
	Description                 pulumi.StringPtrInput
	DisplayName                 pulumi.StringPtrInput
	EmbedHostDomains            pulumi.StringArrayInput
	FeedbackUrl                 pulumi.StringPtrInput
	Name                        pulumi.StringPtrInput
	RedirectUrl                 pulumi.StringPtrInput
	StorageConnectors           StackStorageConnectorArrayInput
	StreamingExperienceSettings StackStreamingExperienceSettingsPtrInput
	Tags                        StackTagArrayInput
	UserSettings                StackUserSettingArrayInput
}

func (StackArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stackArgs)(nil)).Elem()
}

type StackInput interface {
	pulumi.Input

	ToStackOutput() StackOutput
	ToStackOutputWithContext(ctx context.Context) StackOutput
}

func (*Stack) ElementType() reflect.Type {
	return reflect.TypeOf((**Stack)(nil)).Elem()
}

func (i *Stack) ToStackOutput() StackOutput {
	return i.ToStackOutputWithContext(context.Background())
}

func (i *Stack) ToStackOutputWithContext(ctx context.Context) StackOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackOutput)
}

type StackOutput struct{ *pulumi.OutputState }

func (StackOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Stack)(nil)).Elem()
}

func (o StackOutput) ToStackOutput() StackOutput {
	return o
}

func (o StackOutput) ToStackOutputWithContext(ctx context.Context) StackOutput {
	return o
}

func (o StackOutput) AccessEndpoints() StackAccessEndpointArrayOutput {
	return o.ApplyT(func(v *Stack) StackAccessEndpointArrayOutput { return v.AccessEndpoints }).(StackAccessEndpointArrayOutput)
}

func (o StackOutput) ApplicationSettings() StackApplicationSettingsPtrOutput {
	return o.ApplyT(func(v *Stack) StackApplicationSettingsPtrOutput { return v.ApplicationSettings }).(StackApplicationSettingsPtrOutput)
}

func (o StackOutput) AttributesToDelete() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringArrayOutput { return v.AttributesToDelete }).(pulumi.StringArrayOutput)
}

func (o StackOutput) DeleteStorageConnectors() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.BoolPtrOutput { return v.DeleteStorageConnectors }).(pulumi.BoolPtrOutput)
}

func (o StackOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o StackOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.DisplayName }).(pulumi.StringPtrOutput)
}

func (o StackOutput) EmbedHostDomains() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringArrayOutput { return v.EmbedHostDomains }).(pulumi.StringArrayOutput)
}

func (o StackOutput) FeedbackUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.FeedbackUrl }).(pulumi.StringPtrOutput)
}

func (o StackOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o StackOutput) RedirectUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.RedirectUrl }).(pulumi.StringPtrOutput)
}

func (o StackOutput) StorageConnectors() StackStorageConnectorArrayOutput {
	return o.ApplyT(func(v *Stack) StackStorageConnectorArrayOutput { return v.StorageConnectors }).(StackStorageConnectorArrayOutput)
}

func (o StackOutput) StreamingExperienceSettings() StackStreamingExperienceSettingsPtrOutput {
	return o.ApplyT(func(v *Stack) StackStreamingExperienceSettingsPtrOutput { return v.StreamingExperienceSettings }).(StackStreamingExperienceSettingsPtrOutput)
}

func (o StackOutput) Tags() StackTagArrayOutput {
	return o.ApplyT(func(v *Stack) StackTagArrayOutput { return v.Tags }).(StackTagArrayOutput)
}

func (o StackOutput) UserSettings() StackUserSettingArrayOutput {
	return o.ApplyT(func(v *Stack) StackUserSettingArrayOutput { return v.UserSettings }).(StackUserSettingArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StackInput)(nil)).Elem(), &Stack{})
	pulumi.RegisterOutputType(StackOutput{})
}
