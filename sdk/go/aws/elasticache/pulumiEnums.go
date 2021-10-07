// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticache

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Indicates the role of the member, primary or secondary.
type GlobalReplicationGroupMemberRole string

const (
	GlobalReplicationGroupMemberRolePrimary   = GlobalReplicationGroupMemberRole("PRIMARY")
	GlobalReplicationGroupMemberRoleSecondary = GlobalReplicationGroupMemberRole("SECONDARY")
)

func (GlobalReplicationGroupMemberRole) ElementType() reflect.Type {
	return reflect.TypeOf((*GlobalReplicationGroupMemberRole)(nil)).Elem()
}

func (e GlobalReplicationGroupMemberRole) ToGlobalReplicationGroupMemberRoleOutput() GlobalReplicationGroupMemberRoleOutput {
	return pulumi.ToOutput(e).(GlobalReplicationGroupMemberRoleOutput)
}

func (e GlobalReplicationGroupMemberRole) ToGlobalReplicationGroupMemberRoleOutputWithContext(ctx context.Context) GlobalReplicationGroupMemberRoleOutput {
	return pulumi.ToOutputWithContext(ctx, e).(GlobalReplicationGroupMemberRoleOutput)
}

func (e GlobalReplicationGroupMemberRole) ToGlobalReplicationGroupMemberRolePtrOutput() GlobalReplicationGroupMemberRolePtrOutput {
	return e.ToGlobalReplicationGroupMemberRolePtrOutputWithContext(context.Background())
}

func (e GlobalReplicationGroupMemberRole) ToGlobalReplicationGroupMemberRolePtrOutputWithContext(ctx context.Context) GlobalReplicationGroupMemberRolePtrOutput {
	return GlobalReplicationGroupMemberRole(e).ToGlobalReplicationGroupMemberRoleOutputWithContext(ctx).ToGlobalReplicationGroupMemberRolePtrOutputWithContext(ctx)
}

func (e GlobalReplicationGroupMemberRole) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e GlobalReplicationGroupMemberRole) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e GlobalReplicationGroupMemberRole) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e GlobalReplicationGroupMemberRole) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type GlobalReplicationGroupMemberRoleOutput struct{ *pulumi.OutputState }

func (GlobalReplicationGroupMemberRoleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GlobalReplicationGroupMemberRole)(nil)).Elem()
}

func (o GlobalReplicationGroupMemberRoleOutput) ToGlobalReplicationGroupMemberRoleOutput() GlobalReplicationGroupMemberRoleOutput {
	return o
}

func (o GlobalReplicationGroupMemberRoleOutput) ToGlobalReplicationGroupMemberRoleOutputWithContext(ctx context.Context) GlobalReplicationGroupMemberRoleOutput {
	return o
}

func (o GlobalReplicationGroupMemberRoleOutput) ToGlobalReplicationGroupMemberRolePtrOutput() GlobalReplicationGroupMemberRolePtrOutput {
	return o.ToGlobalReplicationGroupMemberRolePtrOutputWithContext(context.Background())
}

func (o GlobalReplicationGroupMemberRoleOutput) ToGlobalReplicationGroupMemberRolePtrOutputWithContext(ctx context.Context) GlobalReplicationGroupMemberRolePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v GlobalReplicationGroupMemberRole) *GlobalReplicationGroupMemberRole {
		return &v
	}).(GlobalReplicationGroupMemberRolePtrOutput)
}

func (o GlobalReplicationGroupMemberRoleOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o GlobalReplicationGroupMemberRoleOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e GlobalReplicationGroupMemberRole) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o GlobalReplicationGroupMemberRoleOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o GlobalReplicationGroupMemberRoleOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e GlobalReplicationGroupMemberRole) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type GlobalReplicationGroupMemberRolePtrOutput struct{ *pulumi.OutputState }

func (GlobalReplicationGroupMemberRolePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GlobalReplicationGroupMemberRole)(nil)).Elem()
}

func (o GlobalReplicationGroupMemberRolePtrOutput) ToGlobalReplicationGroupMemberRolePtrOutput() GlobalReplicationGroupMemberRolePtrOutput {
	return o
}

func (o GlobalReplicationGroupMemberRolePtrOutput) ToGlobalReplicationGroupMemberRolePtrOutputWithContext(ctx context.Context) GlobalReplicationGroupMemberRolePtrOutput {
	return o
}

func (o GlobalReplicationGroupMemberRolePtrOutput) Elem() GlobalReplicationGroupMemberRoleOutput {
	return o.ApplyT(func(v *GlobalReplicationGroupMemberRole) GlobalReplicationGroupMemberRole {
		if v != nil {
			return *v
		}
		var ret GlobalReplicationGroupMemberRole
		return ret
	}).(GlobalReplicationGroupMemberRoleOutput)
}

func (o GlobalReplicationGroupMemberRolePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o GlobalReplicationGroupMemberRolePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *GlobalReplicationGroupMemberRole) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// GlobalReplicationGroupMemberRoleInput is an input type that accepts GlobalReplicationGroupMemberRoleArgs and GlobalReplicationGroupMemberRoleOutput values.
// You can construct a concrete instance of `GlobalReplicationGroupMemberRoleInput` via:
//
//          GlobalReplicationGroupMemberRoleArgs{...}
type GlobalReplicationGroupMemberRoleInput interface {
	pulumi.Input

	ToGlobalReplicationGroupMemberRoleOutput() GlobalReplicationGroupMemberRoleOutput
	ToGlobalReplicationGroupMemberRoleOutputWithContext(context.Context) GlobalReplicationGroupMemberRoleOutput
}

var globalReplicationGroupMemberRolePtrType = reflect.TypeOf((**GlobalReplicationGroupMemberRole)(nil)).Elem()

type GlobalReplicationGroupMemberRolePtrInput interface {
	pulumi.Input

	ToGlobalReplicationGroupMemberRolePtrOutput() GlobalReplicationGroupMemberRolePtrOutput
	ToGlobalReplicationGroupMemberRolePtrOutputWithContext(context.Context) GlobalReplicationGroupMemberRolePtrOutput
}

type globalReplicationGroupMemberRolePtr string

func GlobalReplicationGroupMemberRolePtr(v string) GlobalReplicationGroupMemberRolePtrInput {
	return (*globalReplicationGroupMemberRolePtr)(&v)
}

func (*globalReplicationGroupMemberRolePtr) ElementType() reflect.Type {
	return globalReplicationGroupMemberRolePtrType
}

func (in *globalReplicationGroupMemberRolePtr) ToGlobalReplicationGroupMemberRolePtrOutput() GlobalReplicationGroupMemberRolePtrOutput {
	return pulumi.ToOutput(in).(GlobalReplicationGroupMemberRolePtrOutput)
}

func (in *globalReplicationGroupMemberRolePtr) ToGlobalReplicationGroupMemberRolePtrOutputWithContext(ctx context.Context) GlobalReplicationGroupMemberRolePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(GlobalReplicationGroupMemberRolePtrOutput)
}

// Must be redis.
type UserEngine string

const (
	UserEngineRedis = UserEngine("redis")
)

func (UserEngine) ElementType() reflect.Type {
	return reflect.TypeOf((*UserEngine)(nil)).Elem()
}

func (e UserEngine) ToUserEngineOutput() UserEngineOutput {
	return pulumi.ToOutput(e).(UserEngineOutput)
}

func (e UserEngine) ToUserEngineOutputWithContext(ctx context.Context) UserEngineOutput {
	return pulumi.ToOutputWithContext(ctx, e).(UserEngineOutput)
}

func (e UserEngine) ToUserEnginePtrOutput() UserEnginePtrOutput {
	return e.ToUserEnginePtrOutputWithContext(context.Background())
}

func (e UserEngine) ToUserEnginePtrOutputWithContext(ctx context.Context) UserEnginePtrOutput {
	return UserEngine(e).ToUserEngineOutputWithContext(ctx).ToUserEnginePtrOutputWithContext(ctx)
}

func (e UserEngine) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e UserEngine) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e UserEngine) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e UserEngine) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type UserEngineOutput struct{ *pulumi.OutputState }

func (UserEngineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserEngine)(nil)).Elem()
}

func (o UserEngineOutput) ToUserEngineOutput() UserEngineOutput {
	return o
}

func (o UserEngineOutput) ToUserEngineOutputWithContext(ctx context.Context) UserEngineOutput {
	return o
}

func (o UserEngineOutput) ToUserEnginePtrOutput() UserEnginePtrOutput {
	return o.ToUserEnginePtrOutputWithContext(context.Background())
}

func (o UserEngineOutput) ToUserEnginePtrOutputWithContext(ctx context.Context) UserEnginePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v UserEngine) *UserEngine {
		return &v
	}).(UserEnginePtrOutput)
}

func (o UserEngineOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o UserEngineOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e UserEngine) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o UserEngineOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o UserEngineOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e UserEngine) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type UserEnginePtrOutput struct{ *pulumi.OutputState }

func (UserEnginePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserEngine)(nil)).Elem()
}

func (o UserEnginePtrOutput) ToUserEnginePtrOutput() UserEnginePtrOutput {
	return o
}

func (o UserEnginePtrOutput) ToUserEnginePtrOutputWithContext(ctx context.Context) UserEnginePtrOutput {
	return o
}

func (o UserEnginePtrOutput) Elem() UserEngineOutput {
	return o.ApplyT(func(v *UserEngine) UserEngine {
		if v != nil {
			return *v
		}
		var ret UserEngine
		return ret
	}).(UserEngineOutput)
}

func (o UserEnginePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o UserEnginePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *UserEngine) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// UserEngineInput is an input type that accepts UserEngineArgs and UserEngineOutput values.
// You can construct a concrete instance of `UserEngineInput` via:
//
//          UserEngineArgs{...}
type UserEngineInput interface {
	pulumi.Input

	ToUserEngineOutput() UserEngineOutput
	ToUserEngineOutputWithContext(context.Context) UserEngineOutput
}

var userEnginePtrType = reflect.TypeOf((**UserEngine)(nil)).Elem()

type UserEnginePtrInput interface {
	pulumi.Input

	ToUserEnginePtrOutput() UserEnginePtrOutput
	ToUserEnginePtrOutputWithContext(context.Context) UserEnginePtrOutput
}

type userEnginePtr string

func UserEnginePtr(v string) UserEnginePtrInput {
	return (*userEnginePtr)(&v)
}

func (*userEnginePtr) ElementType() reflect.Type {
	return userEnginePtrType
}

func (in *userEnginePtr) ToUserEnginePtrOutput() UserEnginePtrOutput {
	return pulumi.ToOutput(in).(UserEnginePtrOutput)
}

func (in *userEnginePtr) ToUserEnginePtrOutputWithContext(ctx context.Context) UserEnginePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(UserEnginePtrOutput)
}

// Must be redis.
type UserGroupEngine string

const (
	UserGroupEngineRedis = UserGroupEngine("redis")
)

func (UserGroupEngine) ElementType() reflect.Type {
	return reflect.TypeOf((*UserGroupEngine)(nil)).Elem()
}

func (e UserGroupEngine) ToUserGroupEngineOutput() UserGroupEngineOutput {
	return pulumi.ToOutput(e).(UserGroupEngineOutput)
}

func (e UserGroupEngine) ToUserGroupEngineOutputWithContext(ctx context.Context) UserGroupEngineOutput {
	return pulumi.ToOutputWithContext(ctx, e).(UserGroupEngineOutput)
}

func (e UserGroupEngine) ToUserGroupEnginePtrOutput() UserGroupEnginePtrOutput {
	return e.ToUserGroupEnginePtrOutputWithContext(context.Background())
}

func (e UserGroupEngine) ToUserGroupEnginePtrOutputWithContext(ctx context.Context) UserGroupEnginePtrOutput {
	return UserGroupEngine(e).ToUserGroupEngineOutputWithContext(ctx).ToUserGroupEnginePtrOutputWithContext(ctx)
}

func (e UserGroupEngine) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e UserGroupEngine) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e UserGroupEngine) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e UserGroupEngine) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type UserGroupEngineOutput struct{ *pulumi.OutputState }

func (UserGroupEngineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserGroupEngine)(nil)).Elem()
}

func (o UserGroupEngineOutput) ToUserGroupEngineOutput() UserGroupEngineOutput {
	return o
}

func (o UserGroupEngineOutput) ToUserGroupEngineOutputWithContext(ctx context.Context) UserGroupEngineOutput {
	return o
}

func (o UserGroupEngineOutput) ToUserGroupEnginePtrOutput() UserGroupEnginePtrOutput {
	return o.ToUserGroupEnginePtrOutputWithContext(context.Background())
}

func (o UserGroupEngineOutput) ToUserGroupEnginePtrOutputWithContext(ctx context.Context) UserGroupEnginePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v UserGroupEngine) *UserGroupEngine {
		return &v
	}).(UserGroupEnginePtrOutput)
}

func (o UserGroupEngineOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o UserGroupEngineOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e UserGroupEngine) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o UserGroupEngineOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o UserGroupEngineOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e UserGroupEngine) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type UserGroupEnginePtrOutput struct{ *pulumi.OutputState }

func (UserGroupEnginePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserGroupEngine)(nil)).Elem()
}

func (o UserGroupEnginePtrOutput) ToUserGroupEnginePtrOutput() UserGroupEnginePtrOutput {
	return o
}

func (o UserGroupEnginePtrOutput) ToUserGroupEnginePtrOutputWithContext(ctx context.Context) UserGroupEnginePtrOutput {
	return o
}

func (o UserGroupEnginePtrOutput) Elem() UserGroupEngineOutput {
	return o.ApplyT(func(v *UserGroupEngine) UserGroupEngine {
		if v != nil {
			return *v
		}
		var ret UserGroupEngine
		return ret
	}).(UserGroupEngineOutput)
}

func (o UserGroupEnginePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o UserGroupEnginePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *UserGroupEngine) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// UserGroupEngineInput is an input type that accepts UserGroupEngineArgs and UserGroupEngineOutput values.
// You can construct a concrete instance of `UserGroupEngineInput` via:
//
//          UserGroupEngineArgs{...}
type UserGroupEngineInput interface {
	pulumi.Input

	ToUserGroupEngineOutput() UserGroupEngineOutput
	ToUserGroupEngineOutputWithContext(context.Context) UserGroupEngineOutput
}

var userGroupEnginePtrType = reflect.TypeOf((**UserGroupEngine)(nil)).Elem()

type UserGroupEnginePtrInput interface {
	pulumi.Input

	ToUserGroupEnginePtrOutput() UserGroupEnginePtrOutput
	ToUserGroupEnginePtrOutputWithContext(context.Context) UserGroupEnginePtrOutput
}

type userGroupEnginePtr string

func UserGroupEnginePtr(v string) UserGroupEnginePtrInput {
	return (*userGroupEnginePtr)(&v)
}

func (*userGroupEnginePtr) ElementType() reflect.Type {
	return userGroupEnginePtrType
}

func (in *userGroupEnginePtr) ToUserGroupEnginePtrOutput() UserGroupEnginePtrOutput {
	return pulumi.ToOutput(in).(UserGroupEnginePtrOutput)
}

func (in *userGroupEnginePtr) ToUserGroupEnginePtrOutputWithContext(ctx context.Context) UserGroupEnginePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(UserGroupEnginePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GlobalReplicationGroupMemberRoleOutput{})
	pulumi.RegisterOutputType(GlobalReplicationGroupMemberRolePtrOutput{})
	pulumi.RegisterOutputType(UserEngineOutput{})
	pulumi.RegisterOutputType(UserEnginePtrOutput{})
	pulumi.RegisterOutputType(UserGroupEngineOutput{})
	pulumi.RegisterOutputType(UserGroupEnginePtrOutput{})
}
