// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cognito

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Cognito::UserPoolResourceServer
//
// Deprecated: UserPoolResourceServer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type UserPoolResourceServer struct {
	pulumi.CustomResourceState

	Identifier pulumi.StringOutput                                      `pulumi:"identifier"`
	Name       pulumi.StringOutput                                      `pulumi:"name"`
	Scopes     UserPoolResourceServerResourceServerScopeTypeArrayOutput `pulumi:"scopes"`
	UserPoolId pulumi.StringOutput                                      `pulumi:"userPoolId"`
}

// NewUserPoolResourceServer registers a new resource with the given unique name, arguments, and options.
func NewUserPoolResourceServer(ctx *pulumi.Context,
	name string, args *UserPoolResourceServerArgs, opts ...pulumi.ResourceOption) (*UserPoolResourceServer, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Identifier == nil {
		return nil, errors.New("invalid value for required argument 'Identifier'")
	}
	if args.UserPoolId == nil {
		return nil, errors.New("invalid value for required argument 'UserPoolId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"identifier",
		"userPoolId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource UserPoolResourceServer
	err := ctx.RegisterResource("aws-native:cognito:UserPoolResourceServer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPoolResourceServer gets an existing UserPoolResourceServer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPoolResourceServer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPoolResourceServerState, opts ...pulumi.ResourceOption) (*UserPoolResourceServer, error) {
	var resource UserPoolResourceServer
	err := ctx.ReadResource("aws-native:cognito:UserPoolResourceServer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPoolResourceServer resources.
type userPoolResourceServerState struct {
}

type UserPoolResourceServerState struct {
}

func (UserPoolResourceServerState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolResourceServerState)(nil)).Elem()
}

type userPoolResourceServerArgs struct {
	Identifier string                                          `pulumi:"identifier"`
	Name       *string                                         `pulumi:"name"`
	Scopes     []UserPoolResourceServerResourceServerScopeType `pulumi:"scopes"`
	UserPoolId string                                          `pulumi:"userPoolId"`
}

// The set of arguments for constructing a UserPoolResourceServer resource.
type UserPoolResourceServerArgs struct {
	Identifier pulumi.StringInput
	Name       pulumi.StringPtrInput
	Scopes     UserPoolResourceServerResourceServerScopeTypeArrayInput
	UserPoolId pulumi.StringInput
}

func (UserPoolResourceServerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolResourceServerArgs)(nil)).Elem()
}

type UserPoolResourceServerInput interface {
	pulumi.Input

	ToUserPoolResourceServerOutput() UserPoolResourceServerOutput
	ToUserPoolResourceServerOutputWithContext(ctx context.Context) UserPoolResourceServerOutput
}

func (*UserPoolResourceServer) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolResourceServer)(nil)).Elem()
}

func (i *UserPoolResourceServer) ToUserPoolResourceServerOutput() UserPoolResourceServerOutput {
	return i.ToUserPoolResourceServerOutputWithContext(context.Background())
}

func (i *UserPoolResourceServer) ToUserPoolResourceServerOutputWithContext(ctx context.Context) UserPoolResourceServerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPoolResourceServerOutput)
}

type UserPoolResourceServerOutput struct{ *pulumi.OutputState }

func (UserPoolResourceServerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolResourceServer)(nil)).Elem()
}

func (o UserPoolResourceServerOutput) ToUserPoolResourceServerOutput() UserPoolResourceServerOutput {
	return o
}

func (o UserPoolResourceServerOutput) ToUserPoolResourceServerOutputWithContext(ctx context.Context) UserPoolResourceServerOutput {
	return o
}

func (o UserPoolResourceServerOutput) Identifier() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolResourceServer) pulumi.StringOutput { return v.Identifier }).(pulumi.StringOutput)
}

func (o UserPoolResourceServerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolResourceServer) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o UserPoolResourceServerOutput) Scopes() UserPoolResourceServerResourceServerScopeTypeArrayOutput {
	return o.ApplyT(func(v *UserPoolResourceServer) UserPoolResourceServerResourceServerScopeTypeArrayOutput {
		return v.Scopes
	}).(UserPoolResourceServerResourceServerScopeTypeArrayOutput)
}

func (o UserPoolResourceServerOutput) UserPoolId() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolResourceServer) pulumi.StringOutput { return v.UserPoolId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserPoolResourceServerInput)(nil)).Elem(), &UserPoolResourceServer{})
	pulumi.RegisterOutputType(UserPoolResourceServerOutput{})
}
