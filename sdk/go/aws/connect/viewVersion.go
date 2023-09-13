// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package connect

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Connect::ViewVersion
type ViewVersion struct {
	pulumi.CustomResourceState

	// The version of the view.
	Version pulumi.IntOutput `pulumi:"version"`
	// The description for the view version.
	VersionDescription pulumi.StringPtrOutput `pulumi:"versionDescription"`
	// The Amazon Resource Name (ARN) of the view for which a version is being created.
	ViewArn pulumi.StringOutput `pulumi:"viewArn"`
	// The view content hash to be checked.
	ViewContentSha256 pulumi.StringPtrOutput `pulumi:"viewContentSha256"`
	// The Amazon Resource Name (ARN) of the created view version.
	ViewVersionArn pulumi.StringOutput `pulumi:"viewVersionArn"`
}

// NewViewVersion registers a new resource with the given unique name, arguments, and options.
func NewViewVersion(ctx *pulumi.Context,
	name string, args *ViewVersionArgs, opts ...pulumi.ResourceOption) (*ViewVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ViewArn == nil {
		return nil, errors.New("invalid value for required argument 'ViewArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"versionDescription",
		"viewArn",
		"viewContentSha256",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ViewVersion
	err := ctx.RegisterResource("aws-native:connect:ViewVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetViewVersion gets an existing ViewVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetViewVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ViewVersionState, opts ...pulumi.ResourceOption) (*ViewVersion, error) {
	var resource ViewVersion
	err := ctx.ReadResource("aws-native:connect:ViewVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ViewVersion resources.
type viewVersionState struct {
}

type ViewVersionState struct {
}

func (ViewVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*viewVersionState)(nil)).Elem()
}

type viewVersionArgs struct {
	// The description for the view version.
	VersionDescription *string `pulumi:"versionDescription"`
	// The Amazon Resource Name (ARN) of the view for which a version is being created.
	ViewArn string `pulumi:"viewArn"`
	// The view content hash to be checked.
	ViewContentSha256 *string `pulumi:"viewContentSha256"`
}

// The set of arguments for constructing a ViewVersion resource.
type ViewVersionArgs struct {
	// The description for the view version.
	VersionDescription pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the view for which a version is being created.
	ViewArn pulumi.StringInput
	// The view content hash to be checked.
	ViewContentSha256 pulumi.StringPtrInput
}

func (ViewVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*viewVersionArgs)(nil)).Elem()
}

type ViewVersionInput interface {
	pulumi.Input

	ToViewVersionOutput() ViewVersionOutput
	ToViewVersionOutputWithContext(ctx context.Context) ViewVersionOutput
}

func (*ViewVersion) ElementType() reflect.Type {
	return reflect.TypeOf((**ViewVersion)(nil)).Elem()
}

func (i *ViewVersion) ToViewVersionOutput() ViewVersionOutput {
	return i.ToViewVersionOutputWithContext(context.Background())
}

func (i *ViewVersion) ToViewVersionOutputWithContext(ctx context.Context) ViewVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ViewVersionOutput)
}

func (i *ViewVersion) ToOutput(ctx context.Context) pulumix.Output[*ViewVersion] {
	return pulumix.Output[*ViewVersion]{
		OutputState: i.ToViewVersionOutputWithContext(ctx).OutputState,
	}
}

type ViewVersionOutput struct{ *pulumi.OutputState }

func (ViewVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ViewVersion)(nil)).Elem()
}

func (o ViewVersionOutput) ToViewVersionOutput() ViewVersionOutput {
	return o
}

func (o ViewVersionOutput) ToViewVersionOutputWithContext(ctx context.Context) ViewVersionOutput {
	return o
}

func (o ViewVersionOutput) ToOutput(ctx context.Context) pulumix.Output[*ViewVersion] {
	return pulumix.Output[*ViewVersion]{
		OutputState: o.OutputState,
	}
}

// The version of the view.
func (o ViewVersionOutput) Version() pulumi.IntOutput {
	return o.ApplyT(func(v *ViewVersion) pulumi.IntOutput { return v.Version }).(pulumi.IntOutput)
}

// The description for the view version.
func (o ViewVersionOutput) VersionDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ViewVersion) pulumi.StringPtrOutput { return v.VersionDescription }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the view for which a version is being created.
func (o ViewVersionOutput) ViewArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ViewVersion) pulumi.StringOutput { return v.ViewArn }).(pulumi.StringOutput)
}

// The view content hash to be checked.
func (o ViewVersionOutput) ViewContentSha256() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ViewVersion) pulumi.StringPtrOutput { return v.ViewContentSha256 }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the created view version.
func (o ViewVersionOutput) ViewVersionArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ViewVersion) pulumi.StringOutput { return v.ViewVersionArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ViewVersionInput)(nil)).Elem(), &ViewVersion{})
	pulumi.RegisterOutputType(ViewVersionOutput{})
}
